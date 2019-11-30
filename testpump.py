import sys
import json
import requests
import time
from pprint import pprint

url = 'http://192.168.1.178:8085/api/v1/pump'

for x  in range(300):
    print(x)
    sampleData = {
        "gpio_pin_number": str(x),
        "pump_run_duration": 5,

    }
    req = requests.request('POST', url, data=sampleData)

    print(req.text)
'''
sampleData = {
    "gpio_pin_number": 79,
    "pump_run_duration": 10,
}
req = requests.request('POST', url, data=sampleData)

print(req.text)
'''