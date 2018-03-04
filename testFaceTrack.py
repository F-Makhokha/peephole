import numpy as np
import cv2
import time

face_cascade = cv2.CascadeClassifier('/home/h-o-cally/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
x = 0
y = 0
w = 0
h = 0
xSum = 0
ySum = 0
wSum = 0
hSum = 0
elapsed = 0
current = 0
fps = 0
while(cap.isOpened()):
	current = time.time()
	xSum = 0
	ySum = 0
	wSum = 0
	hSum = 0
	ret, img = cap.read()
	if ret:
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x,y,w,h) in faces:
			xCenter = int(x + w/2)
			yCenter = int(y + w/2)
			xSum += xCenter
			ySum += yCenter
			hSum += h
			wSum += w
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			#roi_gray = gray[y:y+h, x:x+w]
			#roi_color = img[y:y+h, x:x+w]
			
			cv2.circle(img, (xCenter, yCenter), int(min(w, h)/8), (0, 0, 0), -1)	
			cv2.circle(img, (xCenter, yCenter), int((min(w, h)/8) - (min(w, h)/16)), (255, 255, 255), -1)
	if len(faces) > 0:
		radius = int(min(wSum, hSum) / (8 * len(faces)))
		cv2.circle(img, (int(xSum/len(faces)), int(ySum/len(faces))), radius, (255, 255, 255), -1)
		cv2.circle(img, (int(xSum/len(faces)), int(ySum/len(faces))), radius - int(radius/4), (0, 0, 0), -1)
	cv2.imshow('peephole',img)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cap.release()
		cv2.destroyAllWindows()
	elapsed = time.time()
	fps = 1/(elapsed - current)
	print('{:05.2f}'.format(fps), ' FPS, ', len(faces), 'faces in frame')
