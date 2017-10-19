#!/bin/sh -e

# setup ansible
yum install -y git ansible sshpass
rm -rf /etc/ansible
git clone https://github.com/bititanb/ansible-taskmngr /etc/ansible
chmod -R g=u,o=u /etc/ansible

# add jenkins user for jenkins master server
useradd jenkins || true
su -c "ssh-keygen -q -N '' -f /home/jenkins/.ssh/id_rsa" - jenkins

hostnamectl set-hostname taskmngr1
