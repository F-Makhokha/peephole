import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
fps = 69
prevMillis = 0

while(True):
    # Capture frame-by-frame

    currentMillis = int(round(time.time() * 1000))
    ret, frame = cap.read()
    try:
        height, width = frame.shape[:2]
        thumbnail = cv2.resize(frame, (int(width/3), int(height/3)), interpolation = cv2.INTER_AREA)
    # Our operations on the frame come here
        gray = cv2.cvtColor(thumbnail, cv2.COLOR_BGR2GRAY)
        #Display the FPS on frame
        cv2.putText(gray, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)
        cv2.imshow('frame',gray)
        fps = 1000.0 / (currentMillis - prevMillis)
        prevMillis = currentMillis
    except AttributeError:
        print("no vid")
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()                      
