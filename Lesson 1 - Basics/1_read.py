import cv2
import numpy

#reading images
img = cv2.imread('..\Photos\cat.jpg')
cv2.imshow('Cat', img)


# reading videos

capture = cv2.VideoCapture('..\Videos\dog.mp4')
#VideoCapture(0) = Webcam input

#capture=cv2.VideoCapture(0)

while True:
    isTrue,frame=capture.read()

    #width,height = frame.size()


    cv2.circle(frame,(500,500),40,(255,0,0),thickness=2)
    cv2.imshow('Circle',frame)


    #show frame
    cv2.imshow('',frame)

    #if the d key is pressed, kill screen
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()


cv2.waitKey(0)
