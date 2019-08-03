import cv2

out = cv2.VideoWriter('/home/karthik/Karthik/Projects/opencv-instance-segmentation/recorded/output.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 30, (760,616))
cv2.namedWindow("output",cv2.WINDOW_NORMAL);

for i in range(1,3):
    fileName="/home/karthik/Karthik/Projects/opencv-instance-segmentation/recorded/"+str(i)+".mp4"
    cap = cv2.VideoCapture(fileName)
    print(fileName)
    # Check if video opened successfully
    if (cap.isOpened() == False):
        print("Unable to read video feed")
     
    # Default resolutions of the frame are obtained.The default resolutions are system dependent.
    # We convert the resolutions from float to integer.
    
    #frame_width = int(cap.get(3))
    #frame_height = int(cap.get(4)) 
     
    #To find fps
    #fps=cap.get(cv2.CAP_PROP_FPS)
    #print(fps)
    A=True
    while(A):
        ret, frame = cap.read()
        if ret == True: 
        # Display the resulting frame    
            cv2.imshow('output',frame)
            out.write(frame)
        else:
            i=i+1
            A=False
     
        '''# Press q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break''' 
          #cap.release()
          #cv2.destroyAllWindows()

cap.release()    
out.release()
cv2.destroyAllWindows()