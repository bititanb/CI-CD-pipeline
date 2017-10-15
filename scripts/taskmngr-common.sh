#!/bin/sh -e

yum update -y
yum install -y epel-release 
yum install -y neovim

# add deploy user
useradd deploy || true
usermod -p $(openssl passwd deploy) -aG wheel deploy

sed -i 's/^\(SELINUX=\).*/\1disabled/' /etc/selinux/config
