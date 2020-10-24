import os
import delegator
import re
from inspect import isfunction
from subprocess import call

installation_ip_addr = "localhost"
ssh_key_path = "~/.ssh/id_rsa.pub"
remote_user = "root"


def initial_host_configuration():
    ansible_status = check_ansible_host()
    internet_status = check_internet()
    if ansible_status and internet_status:
        return True
    else:
        return False


def check_ansible_host():
    print("\n Checking if ansible is installed on Host Machine")
    check_ansible = delegator.run('which ansible')
    if (check_ansible.out == ""):
        print("> Ansible is not installed")
        return False
    else:
        print("> Ansible Exist.")
        return True


def check_internet():
    print("\n Testing internet Connection")
    dns_output = delegator.run("ping -q -c 1 -W 1 one.one.one.one ")
    if not dns_output.out:
        print("> Internet is not working properly.")
        return False
    else:
        print("> Internet connection looks good.")
        return True


def basic_setup():
    print("\n Creating Network")
    create_doer_network = "ansible-playbook --private-key={} playbooks/create_network.yml -u {} --extra-vars \"variable_host={}\"".format(
        ssh_key_path, remote_user, installation_ip_addr)
    os.system(create_doer_network)

    print("\n Creating Nginx Server")
    create_nginx_proxy = "ansible-playbook --private-key={} playbooks/nginx-proxy.yml -u {} --extra-vars \"variable_host={}\"".format(
        ssh_key_path, remote_user, installation_ip_addr)
    os.system(create_nginx_proxy)

    print("\n Generating certificates")
    gen_certificate = "ansible-playbook --private-key={} playbooks/generate-self-signed-certificates.yml -u {} --extra-vars \"variable_host={}\"".format(
        ssh_key_path, remote_user, installation_ip_addr)
    os.system(gen_certificate)
    return get_input()


def validate_ip(host_ip_ansible):
    ip_regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
    if(re.search(ip_regex, host_ip_ansible)):
        return True

    else:
        return False


def doer_tools():
    install_tools = "ansible-playbook --private-key={} playbooks/tools.yml -u {} --extra-vars \"variable_host={}\"".format(
        ssh_key_path, remote_user, installation_ip_addr)
    os.system(install_tools)
    delegator.run(
        "echo '{}' turtle.doer,en.astroamer.doer,hi.astroamer.doer,te.astroamer.doer,en.icecubes.doer,hi.icecubes.doer,te.icecubes.doer,en.solarsystem.doer,hi.solarsystem.doer,te.solarsystem.doer,solarsystem.doer,linearequation.doer,openstory.doer,runkittyrun.doer,ratiopatterns.doer,agespuzzle.doer,factorisation.doer,musicblocks.doer,physics.doer >> /etc/hosts ".format(installation_ip_addr))
    return get_input()


def portainer():
    install_portainer = "ansible-playbook --private-key={} playbooks/portainer.yml -u {} --extra-vars \"variable_host={}\"".format(
        ssh_key_path, remote_user, installation_ip_addr)
    os.system(install_portainer)
    delegator.run(
        "echo '{}' manage.doer  >> /etc/hosts ".format(installation_ip_addr))
    return get_input()


def wiki():
    install_wiki = "ansible-playbook --private-key={} playbooks/wiki.yml -u {} --extra-vars \"variable_host={}\"".format(
        ssh_key_path, remote_user, installation_ip_addr)
    os.system(install_wiki)
    delegator.run(
        "echo '{}' wiki.doer  >> /etc/hosts ".format(installation_ip_addr))
    return get_input()


def khan():
    install_khan = "ansible-playbook --private-key={} playbooks/khan-academy.yml -u {} --extra-vars \"variable_host={}\"".format(
        ssh_key_path, remote_user, installation_ip_addr)
    os.system(install_khan)
    delegator.run(
        "echo '{}' kolibri.doer  >> /etc/hosts ".format(installation_ip_addr))
    print("\n \n Please visit kolibri.doer and download required resources \n \n")
    return get_input()


def softwares():
    install_softwares = "ansible-playbook --private-key={} playbooks/softwares.yml -u {} --extra-vars \"variable_host={}\"".format(
        ssh_key_path, remote_user, installation_ip_addr)
    os.system(install_softwares)
    delegator.run(
        "echo '{}' software.doer  >> /etc/hosts ".format(installation_ip_addr))
    print("\n \n Please place softwares in /opt/doer/data/softwares directory/folder \n \n")
    return get_input()


def sugar():
    print("Coming soon")
    return get_input()


def quit_program():
    quit()


switcher = {
    1: basic_setup,
    2: portainer,
    3: wiki,
    4: khan,
    5: sugar,
    6: doer_tools,
    7: softwares,
    0: quit_program


}


def numbers_to_strings(argument):
    func = switcher.get(argument, "nothing")
    if isfunction(func):
        return func()
    else:
        return get_input()


def get_input():
    argument = input(
        " \n Select the resource (you want to install: \n 1. Preinstall Configurations \n 2. Portainer ( For managing all websites ) \n 3. Offline Wikipedia \n 4. Khan Academy \n 5. Sugar Labs \n 6. DOER Tools \n 7. Softwares to Download \n \n 0. Quit the installation \n > ")
    print(numbers_to_strings(int(argument)))


def installation_location():
    global ssh_key_path
    global remote_user
    install_location = input(
        "\n Are you running script on same machine where you want to install OER ? (yes/no) > ").upper()
    ssh_key_path = input(
        "\n Please enter path of your ssh keys > ")

    if install_location == 'YES':
        delegator.run("echo 'localhost' >> /etc/ansible/hosts")
        remote_user = input("\n Enter your linux user > ")
        get_input()

    elif install_location == 'NO':
        host_ip_ansible = input(
            "\n Please enter the IP address of machine where you remotely want to install OER > ")
        if validate_ip(host_ip_ansible):
            global installation_ip_addr
            installation_ip_addr = host_ip_ansible
            delegator.run(
                "echo '{}' >> /etc/ansible/hosts".format(installation_ip_addr))
            remote_user = input("\n Enter your remote user > ")
            get_input()
        else:
            print("\n IP address entered was invalid")
            print("\n Please try again")
            installation_location()

    else:
        print("\n Sorry I cannot understand the input !!!")
        print("\n Please try again")
        installation_location()


def main():
    print(" Welcome to DOER 2.0")
    if not os.geteuid() == 0:
        exit("\n Only root can run this script\n")
    print("\n Checking default required configuration")
    if not initial_host_configuration():
        print("#################################")
        print("#Please resolve the above errors#")
        print("#################################")
        exit()
    installation_location()


if __name__ == '__main__':
    main()
