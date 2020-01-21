import time
import sys
import cv2
import numpy as np
import os 
import PumpControl
import timeout_decorator
#########################################################################################
#########################################################################################
  
pumpRunData = {
    "gpio_pin_number": 21,
    "pump_run_duration": 15,
}


#########################################################################################
#########################################################################################
@timeout_decorator.timeout(30)
def DetectFace_Cat(projectDir):
    os.chdir(projectDir)


    print ("OpenCV "+cv2.__version__)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "/usr/local/share/opencv4/haarcascades/haarcascade_frontalcatface_extended.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX
    #id counter
    id = 0
    # names related to ids: example ==> yourname: id=1,  etc
    names = ['None', 'Botmation'] 
    # Initialize and start realtime video capture

    #cam = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM),width=1280, height=720, framerate=21/1, format=NV12 ! nvvidconv flip-method=2 ! video/x-raw,width=960, height=616 format=BGRx ! videoconvert ! appsink' , cv2.CAP_GSTREAMER)
    cam = cv2.VideoCapture(0)
    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    print('Detect')
    pumpDefaultData = {
        "gpio_pin_number": 21,
        "pump_run_duration": 10
    }


    while True:
        time.sleep(1)
        print('loop')
        ret, img =cam.read()
        img = cv2.flip(img, 1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
            )
        for(x,y,w,h) in faces:
            time.sleep(1)
            print('Detect for')
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            #Looks for a specific person
            # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence > 40):
                print('person')
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
                PumpControl.Run_Pump(pumpDefaultData)
                time.sleep(15)
            
            else:
                id = "unknown"
                print(id)
                confidence = "  {0}%".format(round(100 - confidence))
        
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
                
        #cv2.imshow('camera',img) 
        
        #k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        #if k == 27:
        #        break