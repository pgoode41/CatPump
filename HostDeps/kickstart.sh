#!/bin/bash

depsDir='/home/preston/CatPump/HostDeps'

#Set 10Watt(full power)
#Barrel Power only
sudo nvpmodel -m 0

apt install python3-pip -y
apt install nano -y
apt install curl -y
apt install tmux -y

pip3 install Jetson.GPIO

chmod +x "${depsDir}/jetsonSDRezise.sh"
chmod +x "${depsDir}/K3s.sh"
chmod +x "${depsDir}/swapspace.sh"
chmod +x "${depsDir}/installOpenCV4.sh"

"${depsDir}/jetsonSDRezise.sh"
"${depsDir}/K3s.sh"
"${depsDir}/swapspace.sh"
"${depsDir}/installOpenCV4.sh"