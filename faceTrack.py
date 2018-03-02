import numpy as np
import cv2
import time

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()
  
# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
   
# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
    
# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

def scaleToCenter(xCenter, yCenter, _height, _width):
    distanceFromCenterY = yCenter-(_height/2)
    distanceFromCenterX = xCenter-(_width/2)
    return('distance from y: ', distanceFromCenterY, ' distance from x: ', distanceFromCenterX)

face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)


print('Loading')
xCen = 0
yCen = 0

while(True):
    try:
        # Capture frame-by-frame
        ret, frame = cap.read()
        height, width = frame.shape[:2]
    except AttributeError:
        cap = cv2.VideoCapture(0)
        print('.')
        time.sleep(1)
        continue
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Facial recodnition
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        xCen = x+(w/2)
        yCen = y+(h/2)
        print(scaleToCenter(xCen, yCen, height, width))
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()          

