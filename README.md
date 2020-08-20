# DOER
Automated deployment of containers for OpenEducationalResource.

## Installation Instructions
This installation requires a local machine and a remote machine. Local and remote machines can be running on any linux distribution.
> Same local machine can also be used as remote machine if SSH keys for the linux *user* are configured for the localhost.
### Pre-requisite on local machine
* Ansible ([*Install*](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-ubuntu))
* Python3 ([*Install*](https://www.python.org/downloads/))
* Git ([*Install*](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))

### Pre-requisite on remote machine
* Ansible ([*Install*](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-ubuntu))
* Docker ([*Install*](https://docs.docker.com/engine/install/ubuntu/))
* Git ([*Install*](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))

### Install
1. Clone the DOER git repository on local machine.
```
sudo -s
git clone https://github.com/gnowledge/DOER-1.git /var/DOER-1
cd /var/DOER-1
```


2. Create python virtual enviornment and install required libraries on local machine.

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirement.txt
```

3. **Skip** this step if SSH is already configured to access remote machine from local machine: 
* Use below shared steps to new generate SSH keys on local machine and add SSH keys to remote machine.
> Replace below share *user* with username of OS and *hostname* swith appropriate hostname or IP address.
```
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub | ssh user@hostname 'cat >> .ssh/authorized_keys'
```

4. Run the python file on local machine and follow the instructions.
```
python3 main.py 
```
