#!/bin/bash

depsDir='/home/preston/CatPump/HostDeps'

apt install python3-pip -y
apt install nano -y

pip3 install Jetson.GPIO

chmod +x "${depsDir}/jetsonSDRezise.sh"
chmod +x "${depsDir}/K3s.sh"
chmod +x "${depsDir}/swapspace.sh"

"${depsDir}/jetsonSDRezise.sh"
"${depsDir}/K3s.sh"
"${depsDir}/swapspace.sh"