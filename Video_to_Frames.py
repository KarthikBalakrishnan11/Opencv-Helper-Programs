import cv2
import numpy as np

cap=cv2.VideoCapture("cut.mp4")

i=0
skip=1

while(True):
    ret,frames=cap.read()
    if (ret==False):
        break
    skip+=1
    if (skip%20==0):
        #height, width = frames.shape[:2]
        #height=round(0.5*height)
        #width=round(0.5*width)
        #image = cv2.resize(frames,(width, height), interpolation = cv2.INTER_CUBIC)
        #cv2.imshow("frame1",image)
        #cv2.waitKey(0)
        #refPt=[(355, 30), (490, 450)]
        #roi = image[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        i=i+1
        filename="Frames/"+str(i)+".jpg"
        #print(filename)
        #cv2.imshow("roi",roi)
        #cv2.waitKey(0)
        cv2.imwrite(filename,frames)
    
cap.release()
cv2.destroyAllWindows()