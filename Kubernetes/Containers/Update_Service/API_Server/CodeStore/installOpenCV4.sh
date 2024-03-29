#!/bin/bash

#Add swap space for virtual memory ext.



#Purge Open CV Old

apt-get purge libopencv* -y


apt-get update -y
apt-get install -y build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
apt-get install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
apt-get install -y python2.7-dev python3.6-dev python-dev python-numpy python3-numpy
apt-get install -y libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
apt-get install -y libv4l-dev v4l-utils qv4l2 v4l2ucp
apt-get install -y curl
apt install -y python3-pip
apt-get update -y

wget https://github.com/opencv/opencv/archive/4.1.0.zip -O opencv-4.1.0.zip
wget https://github.com/opencv/opencv_contrib/archive/4.1.0.zip -O opencv-contrib-4.1.0.zip
unzip opencv-4.1.0.zip
unzip opencv-contrib-4.1.0.zip
cd opencv-4.1.0/

mkdir release
cd release/
cmake -D WITH_CUDA=ON -D CUDA_ARCH_BIN="5.3" -D CUDA_ARCH_PTX="" -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.1.0/modules -D WITH_GSTREAMER=ON -D WITH_LIBV4L=ON -D BUILD_opencv_python2=ON -D BUILD_opencv_python3=ON -D BUILD_TESTS=OFF -D BUILD_PERF_TESTS=OFF -D BUILD_EXAMPLES=OFF -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
make -j1
make install
apt-get install -y python-opencv python3-opencv

apt-get install -y libjpeg-dev 

pip3 install --user pillow