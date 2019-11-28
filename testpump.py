import sys
import json
import requests
import time
from pprint import pprint

url = 'http://192.168.1.178:8085/api/v1/pump'

for x  in range(1):
    sampleData = {
        "gpio_pin_number": x,
        "pump_run_duration": 10,
    }



    req = requests.request('POST', url, data=sampleData)

    print(req.text)