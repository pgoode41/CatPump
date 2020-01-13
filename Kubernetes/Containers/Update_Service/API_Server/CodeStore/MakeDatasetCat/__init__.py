#Creates facial data set of your face from current camera
import cv2
import os
import numpy as np
#import scp


def MakeDataset_Cat(projectDir):
    #face_detector = cv2.CascadeClassifier("/usr/local/share/opencv4/haarcascades/haarcascade_frontalcatface_extended.xml")
    face_detector = cv2.CascadeClassifier("/usr/local/share/opencv4/haarcascades/haarcascade_frontalcatface_extended.xml")
    #face_detector = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml"')
    # For each person, enter one numeric face id
    face_id = 1
    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    os.chdir(projectDir)
    list = os.listdir('pre-dataset') # dir is your directory path
    print(list)
    number_files = len(list) - 1
    print(number_files)
    count = 0
    #ret, img = cam.read()

    for x in list:
        if x is not '.gitKeep':
            img = cv2.imread(projectDir+'pre-dataset/'+x)
            filesize = os.path.getsize(projectDir+'pre-dataset/'+x)
            if filesize < 15 or filesize is 'None':
                os.remove(projectDir+'pre-dataset/'+x)
                continue
            #print(filesize)

            ##client = scp.Client(host='192.168.1.243', user='preston', password='H@yley41')
            # and then
            #client.transfer(pic, '/home/preston/Documents/catpics')


            #print(x)
            #print(pic)

            #img = cv2.flip(pic, 1) # flip video image vertically
            #print(img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            #print(faces)
            for (x,y,w,h) in faces:
                print('TESTTTTT!!!!!')
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
                count += 1
                # Save the captured image into the pre-datasets folder
                cv2.imwrite(projectDir+"dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
                #cv2.imshow('image', img)
            #if count >= 20:
            #    break

