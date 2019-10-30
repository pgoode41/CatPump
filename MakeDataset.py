#Creates facial data set of your face from current camera
import cv2
import os

#cam = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM),width=1280, height=720, framerate=21/1, format=NV12 ! nvvidconv flip-method=2 ! video/x-raw,width=960, height=616 format=BGRx ! videoconvert ! appsink' , cv2.CAP_GSTREAMER)


face_detector = cv2.CascadeClassifier('/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')
# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count

'''
while(True):
    
    #ret, img = cam.read()
    ret, img = cv2.imread('./pre-dataset')
    img = cv2.flip(img, 1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
'''
list = os.listdir('./pre-dataset') # dir is your directory path
number_files = len(list) - 1
print(number_files)
count = number_files
#ret, img = cam.read()

for x in os.listdir('./pre-dataset'):
    if x is not '.gitKeep':
        ret, img = cv2.imread('./pre-dataset')
        img = cv2.flip(img, 1) # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)
        if count == 4:
            break