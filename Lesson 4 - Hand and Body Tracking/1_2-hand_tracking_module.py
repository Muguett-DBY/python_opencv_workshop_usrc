import cv2
import mediapipe as mp
import time
import numpy as np




class handDetector():
    def __init__(self,mode=False,maxHands=2,detectionConfidence=0.5,trackConfidence=0.5):
        #same parameters for Hand() object in mediapipe
        self.mode=mode
        self.maxHands =maxHands
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands  = self.mpHands.Hands(self.mode, self.maxHands, 
                                         self.detectionConfidence, self.trackConfidence)
        self.mpDraw = mp.solutions.drawing_utils

        self.tipIds = [4,8,12,16,20] #ids for fingertips

    def findHands(self,img,draw=True):
        #convert to RGB
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        #check if hand has been detected
        if self.results.multi_hand_landmarks:
            #draw detected hands
            for handLms in self.results.multi_hand_landmarks:
                #get hand info
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,self.mpHands.HAND_CONNECTIONS)
                #HAND_CONNECTIONS returns the hands with connecting lines



        return img

    def findPosition(self, img,handNo=0, draw=True):

        self.lmList=[]

        #check if hand has been detected
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo] #define a specific hand

            for id, lm in enumerate(myHand.landmark):
                #print(id,lm)
                h, w, c = img.shape #height, width, channels
                cx, cy = int(lm.x*w), int(lm.y*h) #center width, center height
            
                #append position to landmark list
                self.lmList.append([id, cx, cy])

                if draw:
                    cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)

        return self.lmList

    #method to check if fingers are open or closed
    def fingersUp(self):
        fingers = []

        #thumb decision
        if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0]-2][1]: #then fist is open #8 is index end, 6 is index start
            fingers.append(1)
        else:
            fingers.append(0)
            
        for id in range(1,5): #focus on non thumb fingers
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id]-2][2]: #then fist is open #8 is index end, 6 is index start
                fingers.append(1)
            else:
                fingers.append(0)
    
        return fingers



def main():
    cap = cv2.VideoCapture(0) #use webcam

    pTime =0 #previous time
    cTime =0    #current time

    detector= handDetector()

    while True:
        success, img = cap.read()

        #use the find hands method
        detector.findHands(img)

        #find position
        lmList= detector.findPosition(img,draw=False)

        #print location of palm
        if len(lmList) != 0:
            print(lmList[0])

        #determine fps
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime=cTime

        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
        (255,0,255),3)
        
        cv2.imshow("Image", img)
        #cv2.imshow("Black screen",black_screen)
        #black_screen = np.zeros((512,512,3),dtype='uint8')

        #if the d key is pressed, kill screen
        if cv2.waitKey(20) & 0xFF==ord('d'):
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()