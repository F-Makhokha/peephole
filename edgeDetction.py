import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

#    try:
    height, width = frame.shape[:2]
    thumbnail = cv2.resize(frame, (int(width/1), int(height/1)), interpolation = cv2.INTER_AREA)
    # Our operations on the frame come here
    gray = cv2.cvtColor(thumbnail, cv2.COLOR_BGR2GRAY)
        #Display the FPS on frame
    timer = cv2.getTickCount()
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(gray, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)
    cv2.imshow('frame',gray)
	
#    except AttributeError:
#        print("no vid")
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()                      
