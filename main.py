import os
import delegator
import re

def initial_host_configuration():
    ansible_status = check_ansible_host()
    internet_status = check_internet()
    if ansible_status and internet_status:
        return True
    else:
        return False

def check_ansible_host():
    print("Checking if ansible is installed on Host Machine")
    check_ansible = delegator.run('which ansible')
    if (check_ansible.out==""):
        print("> Ansible is not installed")
        return False
    else:
        print("> Ansible Exist.")
        return True

def check_internet():
    print("Testing internet Connection")
    
    # https://unix.stackexchange.com/questions/190513/shell-scripting-proper-way-to-check-for-internet-connectivity
    
    dns_output = delegator.run("ping -q -c 1 -W 1 one.one.one.one ")
    if not dns_output.out:
        print("> Internet is not working properly.")
        return False
    else:
        print("> Internet connection looks good.")
        return True

def validate_ip(host_ip_ansible):
    ip_regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
    if(re.search(ip_regex, host_ip_ansible)):  
        return True  
          
    else:  
        return False  


def installation_location():
    install_location = input("Are you running script on same machine where you want to install OER ? (yes/no) > ").upper()
    if install_location == 'YES':
        print("Push localhost")
        delegator.run("echo 'localhost' >> /etc/ansible/hosts")

    elif install_location =='NO' :
        host_ip_ansible = input("Please enter the IP address of machine where you remotely want to install OER > ")
        if validate_ip(host_ip_ansible) :
            print ("Push IP")
        else:
            print("IP address entered was invalid")
            print("Please try again")
            installation_location()


    else:
        print("Sorry I cannot understand the input !!!")
        print("Please try again")
        installation_location()
       # exit()
        

def main():
    print("Welcome to DOER 2.0")
    if not os.geteuid() == 0:
        exit("\nOnly root can run this script\n")
    print("Checking default required configuration")
    if not initial_host_configuration():
        print("#################################")
        print("#Please resolve the above errors#")
        print("#################################")
        exit()
    installation_location()
    


if __name__ == '__main__':
    main()
    