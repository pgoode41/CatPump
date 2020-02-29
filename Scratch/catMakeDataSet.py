#Creates facial data set of your face from current camera
import cv2
import os



face_detector = cv2.CascadeClassifier('/usr/local/share/opencv4/haarcascades/haarcascade_frontalcatface.xml')
# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")

list = os.listdir('./pre-dataset') # dir is your directory path
number_files = len(list) - 1
print(number_files)
count = 0
#ret, img = cam.read()

for x in os.listdir('./pre-dataset'):
    if x is not '.gitKeep':
        try:
            pic = cv2.imread('./pre-dataset/'+x)
            print(x)
            img = cv2.flip(pic, 1) # flip video image vertically
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
                count += 1
                # Save the captured image into the datasets folder
                cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
                cv2.imshow('image', img)
            if count >= 20:
                break
            pass