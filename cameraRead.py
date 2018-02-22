import cv2
import numpy as np


cap = cv2.VideoCapture(0) #captures from webcam

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('live color',frame)

    if vc2.waitKey(1) and oxFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
