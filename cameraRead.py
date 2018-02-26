import numpy as np
import cv2


def scaleToCenter(xCenter, yCenter, _height, _width):
    distanceFromCenterY = yCenter-_height
    distanceFromCenterX = xCenter-_width
    return('distance from y: ', distanceFromCenterY, ' distance from x: ', distanceFromCenterX)


face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    try:
        xCen = 0
        yCen = 0
        height, width = frame.shape[:2]
        thumbnail = cv2.resize(frame, (int(width/1), int(height/1)), interpolation = cv2.INTER_AREA)
        # Our operations on the frame come here
        gray = cv2.cvtColor(thumbnail, cv2.COLOR_BGR2GRAY)
        # Facial recodnition
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            xCen = x+(w/2)
            yCen = y+(h/2)
        # Display the resulting frame
        cv2.imshow('frame',frame)
        print(scaleToCenter(xCen, yCen, height, width))

    except AttributeError:
        print("no vid")
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()          

