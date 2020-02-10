import RPi.GPIO as GPIO
import time
import requests



GPIO.setmode(GPIO.BOARD)
PIR_PIN = 31
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
                print("Motion Detected!")
                url = "http://192.168.1.46"
                port = ":8085"
                endpoint = '/api/v1/detect/'
                reqDict = request.form.to_dict()
                pprint(reqDict)
                req = requests.request("POST", url+port+endpoint, data=reqDict)
                print(req.text)
                print("Facial Detection De-activated!!!")

print ("PIR Module Test (CTRL+C to exit)")
time.sleep(2)
print ("Ready")

try:
               GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
               while 1:
                              time.sleep(100)
except KeyboardInterrupt:
               print("Quit")
               GPIO.cleanup()

#python3 /opt/CatPump/Motion_Sensor/__init__.py
