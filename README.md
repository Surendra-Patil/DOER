# DOER
DOER is an acronym that expands to Decentralized Distributable Disk of Offline Open Educational Resources. We call it simply DOER instead of the longer abbrev "DDDOOER". With Version 2.0 we have introduced many more features and an easy way to auto-deploy the DOER.

DOER is packaged as a cluster of servers that can be installed on any PC by copying the DOER distribution image of a 1 TB hard disk or just run a script on a machine that will guide you through the installation. 


When we boot from this specially crafted hard disk, the PC boots with several servers that include: NROER (National Repository of Open Educational Resources), Wikipedia in English and Indian languages. Activity-Based Collaborative Distributed Online Courses Online Course Maker and Course Delivery Platform Khan Academy Lite (KALite), PHET Simulations, LOGO, Snap, Edgy (Block based computing platforms), Sugar Learning Environment, and Open Source Software for Education. All the above can be accessed on any browser-enabled device when this DOER installed PC is connected to a LAN of a school or a college. All of them will work without the need for connecting to the Internet.

### ChatShaala

ChatShaala (https://chatshaala.in) is a platform developed, hosted and maintained at Gnowledge Lab, backed by a robust architecture design provided by Discourse. Chatshaala is used collaboratively to do STEM projects and chat about the projects. Investigations and innovation projects are done at Chatshaala. 

### NROER (National Repository of Open Educational Resources)

This is an offline snapshot of the http://nroer.gov.in/ which includes more than 19000 resources on all subjects. It is an initiative of MHRD, Govt of India and CIET NCERT. It brings together digital resources across all stages of school education and teacher education.

More and more resources and features are being added to this platform every month.

Online courses are also served from this platform.

### Online Courses

Activity-based collaborative distributed online courses can be created and published using this server.

The server is integrated with a digital repository to create and manage content (CMS) and a learning management system (LMS). LMS is designed as an interactive system, not merely as a delivery system. Learners could contribute to creating content, participate in peer to peer assessment, rating, discussions, conversations and write blogs.

Activities are composed using digital resources like video, audio or images, assessments and embeddable web-based interactives. Lessons are composed as a sequence of activities. Units are composed as a sequence of lessons Modules are composed of a set of units. Detailed user analytics are available at every unit level.

### H5P
H5P is used to create interactive content for everyone. They can be easily shared, reused and embedded on any website easily.

### Draw.io
Draw.io is used as a board for creating online diagrams. It can be used as a flowchart maker, network diagram software, to create UML online, as an ER diagram tool, to design database schema, to build BPMN online, as a circuit diagram maker etc.

### Drawpile
Drawpile is a collaborative drawing program that allows multiple users to sketch on the same canvas simultaneously.

### Etherpad
Etherpad allows you to edit documents collaboratively in real-time, much like a live multi-player editor that runs in your browser.

### Wetube
It is a free, open source media archive platform based on pan.do/ra. It allows you to manage large, decentralized collections of video, to collaboratively create metadata and time-based annotations, and to serve your archive as a desktop-class web application.

### Nextcloud
It is a file share and collaboration platform. Users can upload their files on nextcloud drive and also share with other users.

### Thingsboard
ThingsBoard is an open-source IoT platform for device management, data collection, processing and visualization for your IoT projects.


### Wikipedia

An offline searchable of Wikipedia.org for selected languages. The offline version is developed and maintained by the Kiwix project (http://www.kiwix.org/).

Presently the default language is English, but there is a provision for other regional languages that can be selected and installed.

### PhET Simulations

PhET provides fun, free, interactive, research-based science and mathematics simulations.

The simulations are developed by Colorado University (https://phet.colorado.edu/en/about).

### KALite (Khan Academy Resources)

An offline version of Khan Academy

KA Lite is open-source software that mimics the online experience of Khan Academy for offline situations. Running KA Lite as a local server, you can watch Khan Academy videos, do Khan exercises, and track student progress -- all without needing an Internet connection!

KA Lite offers instructional videos from Khan Academy on math, science, history, economics and matches the common core standards.

### Sugar Learning Environment

Sugar is both a desktop and a collection of Activities. Activities, as the name implies, are Apps that involve active engagement from the learner. Activities automatically save results to a journal, where reflections are recorded. Activity instances can be shared between learners; many support real-time collaboration.

### Turtle Graphics (Logo programming)

Turtle Blocks is an activity with a Logo inspired graphical "turtle" that draws colorful art based on snap-together visual programming elements. Its "low floor: provides an easy entry point for beginners. It also has "high ceiling" programming features that will challenge the more adventurous.

This is an HTML5 version developed using JavaScript that runs directly in a browser.

### Snap! and Edgy (block-based programming environments)

Snap! is a visual, drag-and-drop programming language. It is an extended re-implementation of Scratch (a project of the Lifelong Kindergarten Group at the MIT Media Lab) that allows you to Build Your Own Blocks. It also features first class lists, first class procedures, and continuations. These added capabilities make it suitable for a serious introduction to computer science for high school or college students. In the example below, a Snap! Users can create new control structures, such as a for loop (which isn’t built into the language), by writing a script as shown at the left. Once the for loop block is created, it can be used even to make nested loops, as shown in the center. A sprite carries out that script at the right.

Edgy is based on Snap to do graphs and networks.


## Installation Instructions
This installation requires two machines, one local machine (from where the script runs) and a remote machine. Local and remote machines can be running on any linux distribution.
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
git clone https://github.com/gnowledge/DOER2.0.git /var/DOER2.0
cd /var/DOER2.0
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
