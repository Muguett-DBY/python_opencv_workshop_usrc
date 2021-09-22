import cv2
import mediapipe as mp
import time

'''for more info, visit:
https://google.github.io/mediapipe/solutions/pose.html'''

cap =  cv2.VideoCapture('../PoseVideos/6.mp4')

cTime=0
pTime=0

mpPose = mp.solutions.pose #define the function path to .pose
pose = mpPose.Pose() #create an object from Pose()
mpDraw = mp.solutions.drawing_utils



while True:
    success, img = cap.read()
    #resize image to fit
    img = cv2.resize(img,(512,342),interpolation=cv2.INTER_AREA)


    #convert img
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = pose.process(imgRGB)
    #print(result.pose_landmarks) #print out attributes for landmarks

    #draw pose frame
    if result.pose_landmarks:
        mpDraw.draw_landmarks(img,result.pose_landmarks,mpPose.POSE_CONNECTIONS)

        #get positional data
        for id, lm in enumerate(result.pose_landmarks.landmark):
            #print(id,lm)
            h, w, c = img.shape #height, width, channels
            cx, cy = int(lm.x*w), int(lm.y*h) #center width, center height
        
            if id ==0: #first landmark
                cv2.circle(img, (cx,cy), 5, (255,0,255), cv2.FILLED)



    #determine fps
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime

    #display fps
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
    (255,0,255),3)

    #display image
    cv2.imshow('Video',img)

    #if the d key is pressed, kill screen
    if cv2.waitKey(1) & 0xFF==ord('d'):
        break

cap.release()
cv2.destroyAllWindows()