import cv2

cap = cv2.VideoCapture("/home/a1036006/Karthik/UPS/Subclips/Jams/Jam9.mp4")
 
cv2.namedWindow("output",cv2.WINDOW_NORMAL);

# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4)) 
#if we want we can use the same h and w in out
 
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
#out = cv2.VideoWriter('ups_output/2018-12-04_01h/Human4.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 15, (960,540))

start_mins='0.27'
start_min_sec=start_mins.split('.')
print(start_min_sec[0],start_min_sec[1])
starts_in_msc=(int(start_min_sec[0])*60+int(start_min_sec[1]))*1000
print(starts_in_msc)
cap.set(cv2.CAP_PROP_POS_MSEC,starts_in_msc)

end_mins='0.37'
end_min_sec=end_mins.split('.')
print(end_min_sec[0],end_min_sec[1])
end_in_msc=(int(end_min_sec[0])*60+int(end_min_sec[1]))*1000
print(end_in_msc)

i=46
skip=1

while(True):
  ret, frame = cap.read()
  cur_position=cap.get(cv2.CAP_PROP_POS_MSEC)
  print("Current position %d milliseconds"%cur_position)
 
  if ret == True: 
    # Display the resulting frame    
    cv2.imshow('output',frame)
    if (skip%10==0):
        #frame = cv2.resize(frame,None,fx=0.5,fy=0.5)
        fileName="/home/a1036006/Karthik/UPS/Subclips/Jams/images/"+str(i)+".jpg"
        print(fileName)
        cv2.imwrite(fileName,frame)
        i=i+1
        
    
    skip=skip+1
    if (cur_position==end_in_msc):
        break
 
    # Press q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
  # Break the loop
  else:
    break 
 
# When everything done, release the video capture and video write objects
cap.release()
#out.release()
 
# Closes all the frames
cv2.destroyAllWindows()