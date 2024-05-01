import numpy as np
import cv2

width_property_id = 3
height_property_id = 4

width_shrink_factor = 0.5
height_shrink_factor = 0.5

#cap = cv2.VideoCapture(0) # from Camera, increase number for more cameras in use
cap = cv2.VideoCapture('assets/sampleVideo_640x360.mp4') # capture

while True:
    ret, frame = cap.read() # return value of capture success/fail, frame = image from video/cam
    cv2.imshow('frame', frame) 
    
    width = int(cap.get(width_property_id)) # convert floating point value to int
    height = int(cap.get(height_property_id))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=width_shrink_factor, fy=height_shrink_factor) # Shrink height and width by half
    # top left
    image[:height//2, :width//2] = cv2.flip(cv2.rotate(smaller_frame, cv2.ROTATE_180),1)
    # top right
    image[height//2:, :width//2] = smaller_frame
    # bottom left
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    # bottom right
    image[height//2:, width//2:] = cv2.flip(smaller_frame, 1)  # Flip along the y-axis (vertical flip)

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'): # returns ascii value of q
        break

cap.release() 
cv2.destroyAllWindows()