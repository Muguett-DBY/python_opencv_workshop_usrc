import numpy as np
import cv2
import os

haarCascade=cv2.CascadeClassifier('haar_face.xml')

people=[]
DIR=r'..\\Faces\\train'
#create list of names by looping through names of folders
for i in os.listdir(DIR):
    people.append(i)

#features =np.load('features.npy')
#labels=np.load('labels.npy')

faceRecognizer=cv2.face.LBPHFaceRecognizer_create()
faceRecognizer.read('face_trained.yml')

img=cv2.imread(r'..\\Faces\\multival.png')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Person',gray)

#detect the face in image
facesRect=haarCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
  
for (x,y,w,h) in facesRect:
    faceROI=gray[y:y+h,x:x+w]

    label,confidence = faceRecognizer.predict(faceROI)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv2.putText(img,str(people[label]),(x,y),
    cv2.FONT_HERSHEY_COMPLEX_SMALL,1.0,(0,255,0),thickness=2 )
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),thickness=2)

cv2.imshow('Detected Face',img)

cv2.waitKey(0)
