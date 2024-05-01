import numpy as np
import cv2
import time
#cap = cv2.VideoCapture(0) # from Camera, increase number for more cameras in use
cap = cv2.VideoCapture('assets/sampleVideo_640x360.mp4') # capture

width_property_id = 3
height_property_id = 4

while True:
    ret, frame = cap.read()
    width = int(cap.get(width_property_id))
    height = int(cap.get(height_property_id))
    
    # draw shapes
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
    
    # write text
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Hey Rabbit!', (10, height - 10), font, 2, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()