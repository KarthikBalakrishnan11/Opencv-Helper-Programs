import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print (w,h)

fps = cap.get(cv2.CAP_PROP_FPS)
print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
num_frames = 120;
     
     
print ("Capturing {0} frames".format(num_frames))
 
    # Start time
start = time.time()
     
    # Grab a few frames
for i in range(0, num_frames) :
    ret, frame = cap.read()
 
     
    # End time
end = time.time()
 
    # Time elapsed
seconds = end - start
print ("Time taken : {0} seconds".format(seconds))
 
    # Calculate frames per second
fps  = num_frames / seconds;
print ("Estimated frames per second : {0}".format(fps))

 
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()