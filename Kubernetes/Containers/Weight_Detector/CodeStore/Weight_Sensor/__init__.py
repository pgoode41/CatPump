#!/usr/bin/env python3
#!/usr/bin/python3



#!/usr/bin/python3



import serial

import time



def Weight_Test():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    while 1: 
        if(ser.in_waiting >0):
            line = ser.readline()
            print(str(line).replace('''\\r\\n''', "").replace("b'", "").replace("'", ""))


