import sys
import json
import requests
from pprint import pprint

url = '192.168.1.178:8085/api/v1/pump'

sampleData = {
    "gpio_pin_number": 12,
    "pump_run_duration": 10,
}

req = requests.request('POST', url, data=sampleData)

print(req)