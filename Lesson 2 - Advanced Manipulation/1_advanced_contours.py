"""
Shape Finding 
The objective is to determine the location of some shape targets on an image. 
To do this, we perform line detection on the image and extract contours.
"""

import cv2
import numpy as np

frame = cv2.imread ('..\Photos/collage.png')
edges = cv2.Canny(frame,100,200) # This uses the canny edge detector. The 100 and 200 are rather arbitrary parameters; the second should be larger than the first, play around to see what numbers work best for each image.

contours, hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
# Get rid of the ones with an area smaller than tiny

#edges.shape returns a tuple containing width and height
blankImage = np.zeros(edges.shape)

goodContours=[]
for contour in contours:
    #check if the contour area is greater than 100 non zero pixels
    if cv2.contourArea(contour)>100:
        goodContours.append(contour)
        #redraw our good contours onto our blank canvas
        #isClosed = is our contour a closed loop
        #color = white
        cv2.polylines(blankImage,contour,isClosed=True,color=(255),thickness=1)

cv2.imshow("original", frame)
cv2.imshow("edges", edges) 
cv2.imshow("big contours", blankImage) 
cv2.waitKey(-1)