#!/bin/bash

#curl -sfL https://get.k3s.io | sh -
#k3s server

#cd ~/Downloads
# Install the CUDA repo metadata that you downloaded manually for L4T
#sudo dpkg -i cuda-repo-l4t-r19.2_6.0-42_armhf.deb
# Download & install the actual CUDA Toolkit including the OpenGL toolkit from NVIDIA. (It only downloads around 15MB)
#sudo apt-get update
# Install "cuda-toolkit-6-0" if you downloaded CUDA 6.0, or "cuda-toolkit-6-5" if you downloaded CUDA 6.5, etc.
#sudo apt-get install cuda-toolkit-6-5
# Install the package full of CUDA samples (optional)
#sudo apt-get install cuda-samples-6-5
# Add yourself to the "video" group to allow access to the GPU
#sudo usermod -a -G video $USER

#sudo dpkg -i cuda-repo-<distro>_<version>_<architecture>.deb

#Installing the CUDA public GPG key

#When installing using the local repo:

#sudo apt-key add /var/cuda-repo-<version>/7fa2af80.pub

##When installing using network repo on Ubuntu 18.04/18.10:

#sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/<distro>/<architecture>/7fa2af80.pub

#When installing using network repo on Ubuntu 16.04:

#sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/<distro>/<architecture>/7fa2af80.pub

#Update the Apt repository cache

sudo apt-get update -y
sudo apt-get upgrade -y

#Install CUDA

#sudo apt-get install cuda



# Add the package repositories
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update -y && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker