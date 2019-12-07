#!/bin/bash

depsDir='/home/preston/CatPump/HostDeps'

#Set 10Watt(full power)
#Barrel Power only
sudo nvpmodel -m 0
udo apt-get purge libopencv* -y
/usr/local/bin/k3s-killall.sh

apt install python3-pip -y
apt install nano -y
apt install curl -y
apt install tmux -y

pip3 install Jetson.GPIO
pip3 install flask
pip3 install pillow

sudo fallocate -l 4.0G /swapfile && sudo chmod 600 /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile
chmod +x "${depsDir}/jetsonSDRezise.sh"
#chmod +x "${depsDir}/K3s.sh"
chmod +x "${depsDir}/swapspace.sh"
chmod +x "${depsDir}/installOpenCV4.sh"

"${depsDir}/jetsonSDRezise.sh"
#"${depsDir}/K3s.sh"
"${depsDir}/swapspace.sh"
"${depsDir}/installOpenCV4.sh"
/usr/local/bin/k3s-killall.sh

#sudo nvidia-docker build API_Server -t pgoode41/catpump-api && sudo nvidia-docker push pgoode41/catpump-api && sudo nvidia-docker pull pgoode41/catpump-api && sudo nvidia-docker run --rm -ti -p 8085:8085 --privileged  pgoode41/catpump-api