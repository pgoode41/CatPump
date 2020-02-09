#!/bin/bash

cd ${CATPUMPDIR}

wget https://raw.githubusercontent.com/tbird20d/grabserial/master/grabserial 

sed -i 's#sd.port = ""#sd.port = "/dev/ttyACM0"#g' grabserial
sed -i 's/sd.baudrate = 115200/sd.baudrate = 9600/g' grabserial
sed -i 's/except getopt.GetoptError, err:/except getopt.GetoptError:/g' grabserial

chmod +x ./grabserial

#python3 grabserial

python3 apiServer.py