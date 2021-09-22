import cv2
import mediapipe as mp
import time
import math


class poseDetector():
    def __init__(self,mode=False,complexity=1,smooth=True,
                detectConfidence=0.5,trackConfidence=0.5):

        #define attributes (same as mediapipe Pose())
        self.mode=mode
        self.complexity=complexity
        self.smooth=smooth
        self.detectConfidence=detectConfidence
        self.trackConfidence=trackConfidence

        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(static_image_mode=self.mode,model_complexity=self.complexity,
                                    smooth_landmarks=self.smooth,min_detection_confidence=self.detectConfidence,
                                    min_tracking_confidence=self.trackConfidence)
        self.mpDraw = mp.solutions.drawing_utils

    def findPose(self,img,draw=True):
        #convert img
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        #print(result.pose_landmarks) #print out attributes for landmarks

        if self.results.pose_landmarks:
            if draw:
                #draw pose frame
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)

        return img

    def findPosition(self, img,draw=True):

        self.lmList=[]

        #check if hand has been detected
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                #print(id,lm)
                h, w, c = img.shape #height, width, channels
                cx, cy = int(lm.x*w), int(lm.y*h) #center width, center height
            
                #append position to landmark list
                self.lmList.append([id, cx, cy])

                if draw:
                    cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)

        return self.lmList

    def findAngle(self,img,p1,p2,p3,draw=True):
        
        #get point coordinates
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        #calculate the angle
        angle = math.degrees(math.atan2(y3-y2,x3-x2)-
                             math.atan2(y1-y2,x1-x2))

        if angle <0:
            angle+= 360

        #draw the desired points and connecting lines
        if draw:
            #circles
            cv2.circle(img,(x1,y1),5,(255,0,0),cv2.FILLED)
            cv2.circle(img,(x1,y1),15,(255,0,0),2)
            cv2.circle(img,(x2,y2),5,(255,0,0),cv2.FILLED)
            cv2.circle(img,(x2,y2),15,(255,0,0),2)
            cv2.circle(img,(x3,y3),5,(255,0,0),cv2.FILLED)
            cv2.circle(img,(x3,y3),15,(255,0,0),2)

            #lines
            cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)
            cv2.line(img,(x3,y3),(x2,y2),(255,0,0),3)

            #text
            cv2.putText(img,str(int(angle)),(x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)


        return angle



def main():
    cap =  cv2.VideoCapture('../PoseVideos/1.mp4')

    pTime =0 #previous time
    cTime =0    #current time

    pose =poseDetector()

    while True:
        success, img = cap.read()
        #resize image to fit
        img = cv2.resize(img,(512,342),interpolation=cv2.INTER_AREA)

        #use find pose method
        pose.findPose(img)

        #find positional data
        lmList=pose.findPosition(img)

        #if len(lmList) != 0:
        #    print(lmList[0])


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

if __name__ == "__main__":
    main()