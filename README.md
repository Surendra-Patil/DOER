# DOER
Automated deployment of containers for OpenEducationResource.

## Installation Instructions

### Pre-requisite
* Docker
* Ansible
* Python3
* Git

### Install
1. Clone the DOER git repo
```
sudo -s
git clone https://github.com/Surendra-Patil/DOER.git /var/DOER
cd /var/DOER
```


2. Create python virtual enviornment and install required libraries.

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirement.txt
```

3. **Skip** this step if SSH is already configured: Generate SSH keys and add SSH keys to remote machine.
> Replace below share user with username of OS and hostname  with appropriate hostname or IP address.
```
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub | ssh user@hostname 'cat >> .ssh/authorized_keys'
```

4. Run the python file and follow the instructions.
```
python3 main.py 
```