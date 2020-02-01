import os
mport sysimport json
import glob
import base64
import requests
import PumpControl
import DetectFaceCat
from flask import Flask
from flask import request
from pprint import pprint
from flask import render_template


app = Flask(__name__)

projectDir = os.environ.get('CATPUMPDIR')
os.chdir(projectDir)
#####################################################################################
#####################################################################################
@app.route('/api/v1/detect/start/', methods=['GET', 'POST'])
def RunPump():
    print("Facial Detection Activated!!!")
    url = "http://192.168.1.46"
    port = ":8085"
    endpoint = '/api/v1/detect/'
    reqDict = request.form.to_dict()
    pprint(reqDict)
    req = requests.request("POST", url+port+endpoint, data=reqDict)
    print("Facial Detection De-activated!!!")
    return "Facial Detection De-activated!!!"
#####################################################################################
#####################################################################################
@app.route('/', methods=['GET', 'POST'])
def root():
    print("root ai_detector hit")
    return "root ai_detector return"
#############################################################
#####################################################################################
if __name__ == '__main__':
    app.run('0.0.0.0', "8095", debug=True)
