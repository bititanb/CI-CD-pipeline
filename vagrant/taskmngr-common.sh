#!/bin/sh -e

# configure /etc/hosts
awk -v ip="192.168.59.2" -v host="taskmngr1" 'BEGIN {FS = OFS = " "} $2 == host {$1 = ip; found = 1}{print} END {if (! found) {print ip, host}}' /etc/hosts > /tmp/awk.out && mv -f /tmp/awk.out /etc/hosts
awk -v ip="192.168.59.2" -v host="testing.taskmngr1" 'BEGIN {FS = OFS = " "} $2 == host {$1 = ip; found = 1}{print} END {if (! found) {print ip, host}}' /etc/hosts > /tmp/awk.out && mv -f /tmp/awk.out /etc/hosts
awk -v ip="192.168.59.3" -v host="taskmngr2" 'BEGIN {FS = OFS = " "} $2 == host {$1 = ip; found = 1}{print} END {if (! found) {print ip, host}}' /etc/hosts > /tmp/awk.out && mv -f /tmp/awk.out /etc/hosts

# add deploy user
useradd deploy || true
usermod -p $(openssl passwd deploy) -aG wheel deploy
sed -i 's/^\(SELINUX=\).*/\1disabled/' /etc/selinux/config

echo 'provisioning successful, rebooting'
(sleep 5 && reboot) &

