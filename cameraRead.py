import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if frame.type() == 1:
        gray = frame
    elif frame.type() == 3:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    elif frame.type() == 4:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('raw', frame)
    cv.imshow('grayscale', gray)

    if cv.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
