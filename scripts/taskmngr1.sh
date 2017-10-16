#!/bin/sh -e

# setup ansible
yum install -y git ansible sshpass
rm -rf /etc/ansible 
git clone https://bitbucket.org/bititanb/taskmngr-ansible /etc/ansible
chmod -R g=u,o=u /etc/ansible

# add jenkins user for jenkins master server
useradd jenkins || true
su -c "ssh-keygen -q -N '' -f /home/jenkins/.ssh/id_rsa" - jenkins 
