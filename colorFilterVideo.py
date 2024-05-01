import numpy as np
import cv2

#cap = cv2.VideoCapture(0) # from Camera, increase number for more cameras in use
cap = cv2.VideoCapture('assets/sampleVideo_640x360.mp4') # capture

width_property_id = 3
height_property_id = 4

while True:
    ret, frame = cap.read()
    width = int(cap.get(width_property_id))
    height = int(cap.get(height_property_id))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # bgr -> hsv (hue saturation value)
    # cv2.imshow('frame', hsv)
    
    bgr_clr = np.array([[[0, 255, 0]]], dtype = np.uint8) # green color pixel in BGR
    x = cv2.cvtColor(bgr_clr, cv2.COLOR_BGR2HSV) 
    print(x[0][0]) # green color pixel in HSV = [60 255 255]
    
    lower_green = np.array([30, 50, 50]) # lower bound
    upper_green = np.array([90, 255, 255]) # upper bound
    
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    result = cv2.bitwise_and(frame, frame, mask=mask) # Keep the pixels that return 1 aka same in both videos sources
    
    cv2.imshow('frame', result)
    # cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
