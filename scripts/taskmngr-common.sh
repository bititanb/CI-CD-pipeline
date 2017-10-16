#!/bin/sh -e

yum install -y epel-release 
yum install -y neovim

# add regular user with sudo access
useradd user1 || true
usermod -p $(openssl passwd 1) -aG wheel user1

# add deploy user
useradd deploy || true
usermod -p $(openssl passwd deploy) -aG wheel deploy

sed -i 's/^\(SELINUX=\).*/\1disabled/' /etc/selinux/config
