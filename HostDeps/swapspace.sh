#!/bin/bash

#Add swap space for virtual memory ext.

fallocate -l 4.0G /swapfile 
chmod 600 /swapfile 
mkswap /swapfile 
swapon /swapfile
echo >> /swapfile none swap 0 0


