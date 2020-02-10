import os
import json
import glob
import base64
import requests
import Weight_Sensor
from flask import Flask
from flask import request
from pprint import pprint
from flask import render_template


app = Flask(__name__)

projectDir = os.environ.get('CATPUMPDIR')
os.chdir(projectDir)
#####################################################################################
#####################################################################################
@app.route('/api/v1/weight/detect/start/single', methods=['GET', 'POST'])
def Weigh_Single():
    print("Weigh_Single() hit!")
    #Weight_Sensor.Weight_Test_Single()
    #return Weight_Sensor.Weight_Test_Single()
    return Weight_Sensor.Weight_Test_Single()
#####################################################################################
#####################################################################################
@app.route('/', methods=['GET', 'POST'])
def root():
    print("root weight_detector hit")
    Weight_Sensor.Weight_Test_Loop()
    return "root weight_detector return"
#############################################################
#####################################################################################
@app.route('/api/v1/weight/detect/start/loop', methods=['GET', 'POST'])
#NOT WORKING
#ONLY RETURN SINGLE
def Weigh_Loop():
    print("Weigh_Loop() hit!")
    return Weight_Sensor.Weight_Test_Loop()
#####################################################################################
#####################################################################################
if __name__ == '__main__':
    app.run('0.0.0.0', "8055", debug=True)
