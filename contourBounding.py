import numpy as np
import cv2

xPos = 0
yPos = 0
x = 0
y = 0
w = 0
h = 0
cap = cv2.VideoCapture(0)
fps = 0
while(True):
    #Start FPS timer at beginning of loop
    timer = cv2.getTickCount()

    # Capture frame-by-frame
    ret, frame = cap.read()
    height, width = frame.shape[:2]
    xPos = width/2
    yPos = height/2
    frame = cv2.resize(frame, (int(width/1), int(height/1)), interpolation = cv2.INTER_AREA)
	
    # Our operations on the frame come here
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.inRange(frame, (100, 0.0, 0.0), (255, 32.037, 66.67232))
    im2, contours, hi = cv2.findContours(frame, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
	contours = filter(lambda x: cv2.contourArea(x) > 1000, contours)	
    if len(contours) != 0:
	cv2.drawContours(frame, contours, -1, (255, 255, 0), 1)
	c = max(contours, key = cv2.contourArea)
	x, y, w, h = cv2.boundingRect(c)
	xPos = x - width/2 + w/2
	yPos = y - height/2 + h/2
	cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
    #Displays frame
    print(xPos, yPos)
    cv2.circle(frame, (x+w/2, y+h/2), (min([w, h])/8), (100, 100, 100), -1)
    cv2.imshow('peephole', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
