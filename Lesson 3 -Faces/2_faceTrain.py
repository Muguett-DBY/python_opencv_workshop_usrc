import cv2
import os 
import numpy as np
import matplotlib.pyplot as plt


people=[]

DIR=r'..\\Faces\\train'
#create list of names by looping through names of folders
for i in os.listdir(DIR):
    people.append(i)
print(people)


#store the haar face database to haarCascade
haarCascade=cv2.CascadeClassifier('haar_face.xml')

features = [] #faces
labels = [] #names for faces


def create_train():
    for person in people:
        #path to folder containing the person
        path = os.path.join(DIR,person)
        #returns the index of the specified element
        label = people.index(person)

        for img in os.listdir(path):
            #find path for individual image
            imgPath= os.path.join(path,img)

            #read image
            imgArray = cv2.imread(imgPath)
            gray = cv2.cvtColor(imgArray,cv2.COLOR_BGR2GRAY)

            #create rectangle for face
            facesRect=haarCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            #grab a region of interest of the face 
            #store in arrays
            for (x,y,w,h) in facesRect:
                faceROI=gray[y:y+h,x:x+w]
                features.append(faceROI)
                labels.append(label)


create_train()
print('Training Done ---------------')


features=np.array(features,dtype='object')
labels=np.array(labels)

faceRecognizer=cv2.face.LBPHFaceRecognizer_create()


#train the recognizer using features list and labels list
faceRecognizer.train(features,labels)

#save the model
faceRecognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)

