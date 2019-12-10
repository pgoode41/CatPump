import os
import sys
import json
import glob
import base64
import requests
import PumpControl
import TrainFaceCat
import DetectFaceCat
import MakeDatasetCat
from flask import Flask
from flask import request
from pprint import pprint
from flask import render_template



app = Flask(__name__)

projectDir = os.environ.get('CATPUMPDIR')
os.chdir(projectDir)
UPLOAD_FOLDER = projectDir+'./pre-dataset' 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
#####################################################################################
#####################################################################################
@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('ImageUpload.html')
#####################################################################################
#####################################################################################
@app.route('/api/v1/data/upload', methods=['GET', 'POST'])
def Model_Save():
    try:
        os.remove('./dataset/.gitKeep')
        os.remove('./pre-dataset/.gitKeep')
        os.remove('./trainer/.gitKeep')
    except:
        pass
    files = request.files
    picCounter = 0
    for x in files:
        print(x)
        file = request.files[x]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],'cat-pic-'+str(picCounter)+'.jpeg'))
        picCounter += 1

    #Prime pump
    pumpPrimeData = {
        "gpio_pin_number": 21,
        "pump_run_duration": 10
    }
    print("Priming Pump")
    PumpControl.Run_Pump(pumpPrimeData)
    PumpControl.Run_Pump(pumpPrimeData)
    PumpControl.Run_Pump(pumpPrimeData)
    print('Pump has been primed.')

    MakeDatasetCat.MakeDataset_Cat(projectDir)
    TrainFaceCat.TrainModle_Cat(projectDir)
    DetectFaceCat.DetectFace_Cat(projectDir)

    return "Return Message From /api/v1/data/upload."
#####################################################################################
#####################################################################################
@app.route('/api/v1/pump', methods=['GET', 'POST'])
def RunPump():
    #PumpControl()
    reqDict = request.form.to_dict()
    pprint(reqDict)
    #reqDict = json.loads(req)
    return PumpControl.Run_Pump(reqDict)
#####################################################################################
#####################################################################################


#############################################################
#####################################################################################
if __name__ == '__main__':
    app.run('0.0.0.0', "8085", debug=True)
