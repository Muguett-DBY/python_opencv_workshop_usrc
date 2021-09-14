"""
Shape Finding 2
Great! We have less random noise and more shapes now. Next, we have to find all those hearts! Perhaps if we had a 
heart template, we could match the hearts in the image to the heart template. But all the hearts are of different sizes and rotations...

Fortunately, people smarter than we figured out that certain functions of the x and y coordinates of an image are 
invariant to the size, scaling and rotation of a shape. These are called the Hu-moments of the image, and we'll use them 
to our advantage here.
"""

import cv2
import numpy as np

frame = cv2.imread ('..\Photos/collage.png')
edges = cv2.Canny(frame,100,200) # This uses the canny edge detector. The 100 and 200 are rather arbitrary parameters; the second should be larger than the first, play around to see what numbers work best for each image.


# Load another heart from a template
heart = cv2.imread('..\Photos\heart.png')
heartCanny = cv2.Canny(heart,100,200) #make a canny
heartContours, hierarchy = cv2.findContours(heartCanny,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE) #find the contours of our heart image
#hierarchy denotes which contours are parents and the children of those parent contours

heartBlank = np.zeros(heart.shape)
cv2.polylines(heartBlank,heartContours,True,(255),1)
# Find its contours and create a moment set for checking

heartMoments = cv2.moments(heartContours[1]) #moment is average of intensities, which allows us to get the center of a contour
heartHuMoments= cv2.HuMoments(heartMoments)

'''
https://learnopencv.com/tag/hu-moments/

Hu Moments ( or rather Hu moment invariants ) are a set of 7 
numbers calculated using central moments that are invariant to
 image transformations. The first 6 moments have been proved to 
 be invariant to translation, scale, and rotation, and reflection. 
 While the 7th moment’s sign changes for image reflection.
'''

print("heartHuMoments:\n",heartHuMoments,"\n")

contours, hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
# Get rid of the ones with an area smaller than tiny

blankImage = np.zeros(edges.shape)

goodContours=[]
for contour in contours:
    if cv2.contourArea(contour)>100:
        contourMoments = cv2.moments(contour)
        contourHuMoments = cv2.HuMoments(contourMoments)
        #find the difference between moments
        delta = np.sum(heartHuMoments-contourHuMoments)
        print(delta)
        if (np.abs(delta)<0.002): #0.002 is our threshold
            print(np.abs(delta))
            goodContours.append(contour)
            cv2.polylines(blankImage,contour,True,(255),1)

#cv2.imshow("original", frame)
cv2.imshow("heart", heartBlank)
cv2.imshow("heartContour", heartCanny)
cv2.imshow("edges", edges) 
cv2.imshow("good contours", blankImage) 
cv2.waitKey(-1)


####Exercises####
# Instead of filtering for the heart, instead filter for a pentagon, look in the file folder!
