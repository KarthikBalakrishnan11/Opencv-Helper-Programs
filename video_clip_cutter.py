import cv2
 
# Create a VideoCapture object
cap = cv2.VideoCapture("ups_videos/2018-12-04_01h.mp4")
 
cv2.namedWindow("output",cv2.WINDOW_NORMAL);

# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4)) #if we want we can use the same h and w in out
 
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
#out = cv2.VideoWriter('ups_output/2018-11-20_05h/Jam1.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 15, (frame_width,frame_height))
out = cv2.VideoWriter('ups_output/2018-12-04_01h/Human4.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 15, (960,540))

start_mins=59
starts_in_msc=start_mins*60*1000
cap.set(cv2.CAP_PROP_POS_MSEC,starts_in_msc)

end_mins=60

while(True):
  ret, frame = cap.read()
  cur_position=cap.get(cv2.CAP_PROP_POS_MSEC)
  cur_position=int((cur_position/1000)/60)
  print("Current position %d mins"%cur_position)
 
  if ret == True: 
     # Display the resulting frame    
    cv2.imshow('output',frame)
    frame = cv2.resize(frame,None,fx=0.5,fy=0.5)
    out.write(frame)


    if (cur_position==end_mins):
        break
 
    # Press q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
  # Break the loop
  else:
    break 
 
# When everything done, release the video capture and video write objects
cap.release()
out.release()
 
# Closes all the frames
cv2.destroyAllWindows()