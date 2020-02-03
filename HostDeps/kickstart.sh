#!/bin/bash

depsDir='/home/preston/CatPump/HostDeps'


apt install python3-pip -y
apt install nano -y
apt install curl -y
apt install tmux -y

pip3 install Jetson.GPIO
pip3 install flask

chmod +x "${depsDir}/jetsonSDRezise.sh"
chmod +x "${depsDir}/Configure_Services.sh"
#chmod +x "${depsDir}/K3s.sh"

"${depsDir}/jetsonSDRezise.sh"
"${depsDir}/K3s.sh"&
"${depsDir}/Configure_Services.sh"
