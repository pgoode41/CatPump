import os
import sys
import json
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
@app.route('/api/v1/detect/start', methods=['GET', 'POST'])
def RunPump():
    print("Facial Detection Activated!!!")
    DetectFaceCat.DetectFace_Cat(projectDir)
    print("Facial Detection De-activated!!!")
    return "Facial Detection De-activated!!!"
#####################################################################################
#####################################################################################


#############################################################
#####################################################################################
if __name__ == '__main__':
    app.run('0.0.0.0', "8095", debug=True)
