#!/bin/bash

depsDir='/home/preston/catpump/HostDeps'

chmod +x "${depsDir}/jetson_full_power.sh"
chmod +x "${depsDir}/swapspace.sh"
chmod +x "${depsDir}/jetsonSDRezise.sh"

"${depsDir}/jetson_full_power.sh"
"${depsDir}/jetsonSDRezise.sh"
"${depsDir}/swapspace.sh"

apt upgrade -y 
apt install python3-pip -y
apt install nano -y
apt install curl -y
apt install tmux -y

pip3 install Jetson.GPIO
pip3 install flask

cat ${depsDir}/docker_password.txt | docker login --username pgoode41 --password-stdin


chmod +x "${depsDir}/Configure_Services.sh"
chmod +x "${depsDir}/Start_All_Containers.sh"
chmod +x "${depsDir}/pump_boot_actions.py"
#chmod +x "${depsDir}/K3s.sh"

#RUN ORDER IS VERY IMPORTANT!
"${depsDir}/pump_boot_actions.py"
#"${depsDir}/K3s.sh"&
"${depsDir}/Start_All_Containers.sh"
"${depsDir}/Configure_Services.sh"
