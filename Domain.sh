#!/bin/bash

sudo hostnamectl set-hostname $1.$2;
sudo sh -c "echo 127.0.0.1  $1.$2 $1 >> /etc/hosts";
sudo sh -c "echo search $2 >> /etc/resolv.conf";
sudo sh -c "echo nameserver $3 >> /etc/resolv.conf";

sudo dnf install join-to-domain && join-to-domain.sh -d $2 -n $1 -u $4 -p $5;i
