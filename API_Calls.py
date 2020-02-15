import os 
import sys
import requests
from pprint import pprint
import json
###########################################################################
###########################################################################
class CatPump_Api:
    def __init__(self):
        print("in init")
    def StartPump():
        print("Calling to CatPump_Ai-Api Micro-Service")
        url = "http://192.168.1.46"
        port = ":8085"
        endpoint = "/api/v1/pump/start/"
        data = {
            "gpio_pin_number": 21,
            "pump_run_duration": 5
        }
        req = requests.request("POST", url+port+endpoint, data=data)
        print(req.text)
###########################################################################
###########################################################################
class CatPump_MotionSensor:

    def MotionData(self):
        print("Calling to CatPump_MotionSensor Micro-Service")
###########################################################################
###########################################################################
class CatPump_WeightSensor:
    def __init__(self):
        print("in init")
    def GetWeight():
        print("Calling to CatPump_WeightSensor Micro-Service")
        url = "http://192.168.1.46"
        port = ":8055"
        endpoint = "/api/v1/weight/detect/start/single"
        req = requests.request("GET", url+port+endpoint)
        print(req.text)
###########################################################################
###########################################################################
class CatPump_Updater:

    def ApplyUpdate(self):
        print("Calling to CatPump_Updater Micro-Service")
###########################################################################
###########################################################################

CatPump_Api.StartPump()


CatPump_WeightSensor.GetWeight()
