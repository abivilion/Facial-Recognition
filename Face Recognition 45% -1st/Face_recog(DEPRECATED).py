import cv2
import numpy as np
import os
# // MADE By: Ayush Bhardwaj
# // ABIVILION

recognizer = cv2.face.LBHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade=cv2.CascadeClassifier(cascadePath)


font = cv2.FONT_HERSHEY_PLAIN

id=0

names=[0,1,2,3,4,5]
cam.cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

#minimumm width
minW=0.1*cam.get(3)
# minimum heigth
minH=0.1*cam.get(4)

while True:
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BAYER_BG2BGR)
    faces=faceCascade.detectMultiScale(gray,
    scaleFactor=1.2,
    minNeighbors=len(names))
    minSize=(int(minW),int(minH)),
    

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w,y+h),(255,255,255),2)
        id,confid = recognizer.predict(gray[y:y+h,x:x+w])

        if(confid<100):
            id=names[id]
            confid=f"{100-confid}% "
        else:
            id="unknown"
            confid=f"{100-confid}% "
        cv2.putText(img,str(id),(x+5,y+5),font,1,(255,255,255),2)
        cv2.putText(img,str(confid),(x+5,y+h-5),font,1,(255,255,255),1)
    cv2.imshow('camera',img)

    k=cv2.waitkey(10) & 0xff

    if k==27: #wait for 27sec
        break;

print("\n [INFO] Exiting program")
cam.release()
cv2.destroyAllWindows()


