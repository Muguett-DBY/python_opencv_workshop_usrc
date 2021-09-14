import cv2
import numpy

#reading images
img = cv2.imread('Photos/car.jpg')
cv2.imshow('car', img)
cv2.waitKey(0)
