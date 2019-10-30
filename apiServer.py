import os
import sys
import base64
import requests
from flask import Flask
from flask import request
from pprint import pprint
from flask import render_template

from flask import Flask
app = Flask(__name__)
UPLOAD_FOLDER = './pre-dataset' 
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
    os.remove('./dataset/.getKeep')
    os.remove('./pre-dataset/.getKeep')
    os.remove('./trainer/.getKeep')
    files = request.files
    picCounter = 0
    for x in files:
        print(x)
        file = request.files[x]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],'cat-pic-'+str(picCounter)+'.jpg'))
        picCounter += 1

    return "Return Message From /api/v1/data/upload."
#####################################################################################
#####################################################################################
#############################################################
#####################################################################################
if __name__ == '__main__':
    app.run('0.0.0.0', "8085", debug=True)


