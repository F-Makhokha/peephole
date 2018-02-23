import numpy as np
import cv2


cap = cv2.VideoCapture(0)
fps = 0

while(True):
    #Start FPS timer at beginning of loop
    timer = cv2.getTickCount()

    # Capture frame-by-frame
    ret, frame = cap.read()
    try:
	height, width = frame.shape[:2]
	frame = cv2.resize(frame, (int(width/1), int(height/1)), interpolation = cv2.INTER_AREA)
	
	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	_ ,gray = cv2.threshold(gray, 150, 0, cv2.THRESH_TOZERO)

	#Display the FPS on frame
	cv2.putText(gray, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)	
	fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
	
	#Displays frame
	cv2.imshow('peephole',gray)
    except AttributeError:
	print("No Video")
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()                      
