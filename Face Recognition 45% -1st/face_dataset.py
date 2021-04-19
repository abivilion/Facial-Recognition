
import cv2
import os

# // MADE By: Ayush Bhardwaj
# // ABIVILION


cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n Enter User Identification Number: ')
Facial_Storage = int(input("Quantity for Each person should be clicked and stored - "))


print("\n [INFO] Initializing face capture....")
# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cam.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff 
    if k == Facial_Storage:
        print("xrwr34242423")
        break;
    elif count >= Facial_Storage: 
        print(90000)
        break;

# Do a bit of cleanup
print("\n [INFO] Exiting Program")
cam.release()
cv2.destroyAllWindows()


