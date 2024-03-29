import cv2
import numpy as np
from PIL import Image #pip install pillow ; also need sudo apt-get install libjpeg-dev
import os

def TrainModle_Cat(projectDir):
    os.chdir(projectDir)
    # Path for face image database
    path = 'dataset'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("/usr/local/share/opencv4/haarcascades/haarcascade_frontalcatface_extended.xml")
    # function to get the images and label data
    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
        faceSamples=[]
        ids = []
        idCount = 0
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
            img_numpy = np.array(PIL_img,'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            #id = idCount
            idCount += 1
            faces = detector.detectMultiScale(img_numpy)
            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
        return faceSamples,ids
    print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces,ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))
    # Save the model into trainer/trainer.yml
    try:
        os.mkdir(projectDir+'trainer')
    except:
        pass
    #os.mkdir(projectDir+'trainer')
    print(projectDir+'trainer/trainer.yml')
    recognizer.write(projectDir+'trainer/trainer.yml') 
    # Print the numer of faces trained and end program
    print('Training Completed')
    #print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))