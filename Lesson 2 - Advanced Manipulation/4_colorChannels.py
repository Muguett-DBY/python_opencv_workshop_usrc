import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('../Photos/park.jpg')

blank=np.zeros(img.shape[:2],dtype='uint8')

b,g,r=cv2.split(img) #split the image into rgb

blue=cv2.merge([b,blank,blank]) #merge combines pixel values
green=cv2.merge([blank,g,blank])
red=cv2.merge([blank,blank,r])

cv2.imshow('Blue',blue)
cv2.imshow('Green',green)
cv2.imshow('Red',red)



cv2.waitKey(0)