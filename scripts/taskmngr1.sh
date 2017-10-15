#!/bin/sh -e

yum install -y git ansible sshpass

rm -rf /etc/ansible 
git clone https://bitbucket.org/bititanb/taskmngr-ansible /etc/ansible
chmod -R g=u,o=u /etc/ansible

useradd jenkins || true
su -c "ssh-keygen -q -N '' -f /home/jenkins/.ssh/id_rsa" - jenkins 
