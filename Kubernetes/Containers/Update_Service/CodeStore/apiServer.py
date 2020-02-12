import os
import sys
import json
import glob
import base64
import requests
import HostConfig
from flask import Flask
from flask import request
from pprint import pprint
from flask import render_template




app = Flask(__name__)

projectDir = os.environ.get('CATPUMPDIR')
os.chdir(projectDir)
#####################################################################################
#####################################################################################
@app.route('/api/v1/updates', methods=['GET', 'POST'])
def UpdateDevice():
    print("Updating Device")
    updatesFolder = projectDir+"Updates"

    os.mkdir(updatesFolder)
    os.chdir(updatesFolder)
    updateFile = open(updatesFolder, "w")
    updateFile.write("Test Update From Update Service Container API")
    updateFile.close()

    return "Device Update Completed."
#####################################################################################
#####################################################################################
@app.route('/', methods=['GET', 'POST'])
def root():
    print("root update_service hit")
    HostConfig.TestPlay()
    return "root update_service hit"

#############################################################
#####################################################################################
if __name__ == '__main__':
    app.run('0.0.0.0', "8076", debug=True)
