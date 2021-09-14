import cv2
import numpy as np

frame= cv2.imread ('..\Photos/collage.png')
edges=cv2.Canny(frame,100,200)

# Load another heart from a template
heart = cv2.imread('..\Photos\heart.png')
heartCanny=cv2.Canny(heart,100,200)
heartContours, hierarchy = cv2.findContours(heartCanny,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

heartBlank = np.zeros(heart.shape)
cv2.polylines(heartBlank,heartContours,True,(255),1)

heartMoments = cv2.moments(heartContours[1])
heartHuMoments= cv2.HuMoments(heartMoments) 

contours, hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

blankImage=np.zeros(edges.shape)

goodContours=[]
for contour in contours:
    if cv2.contourArea(contour)>100:

        contourMoments = cv2.moments(contour)
        contourHuMoments = cv2.HuMoments(contourMoments)

        #find the difference between moments
        delta = np.sum(heartHuMoments-contourHuMoments)

        if (np.abs(delta)<0.002): #0.002 is our threshold
            goodContours.append(contour)
            cv2.polylines(blankImage,contour,isClosed=True,color=(255),thickness=1)


cv2.imshow("original", frame)
cv2.imshow("heart", heartBlank)
cv2.imshow("edges", edges) 
cv2.imshow("big contours", blankImage) 
cv2.waitKey(-1)