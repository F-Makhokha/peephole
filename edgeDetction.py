import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
fps = 69
prevMillis = 0
height = 500
width = 500
print("Loading")
while(True):
    # Capture frame-by-frame
    try:
        ret, frame = cap.read()
        height, width = frame.shape[:2]
    except AttributeError:
        cap = cv2.VideoCapture(0)
        print(".")
        time.sleep(1)
        continue
    thumbnail = cv2.resize(frame, (int(width/3), int(height/3)), interpolation = cv2.INTER_AREA)
    # Our operations on the frame come here
    gray = cv2.cvtColor(thumbnail, cv2.COLOR_BGR2GRAY)
    #Display the FPS on frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()                      
