import numpy as np
import cv2

line_thickness = 2 

gray_scale_id = 0

# The image to be matched must be closer to the side of the object in the base image

img = cv2.resize(cv2.imread('assets/soccer_practice.jpg'), (0, 0), fx=0.8, fy=0.8)
img1 = cv2.resize(cv2.imread('assets/soccer_practice.jpg', gray_scale_id), (0, 0), fx=0.8, fy=0.8)
template = cv2.resize(cv2.imread('assets/ball.PNG', gray_scale_id), (0, 0), fx=0.8, fy=0.8)
h, w = template.shape # -> (height, weight)

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods: # loop through all methods and find the right one
    img2 = img1.copy()
    
    # convolution: 2d array resulting match in each region of img2 by sliding template image through it: (W-w+1, H-h+1)
    result = cv2.matchTemplate(img2, template, method) 
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h) # moving through the original image
    # Colored img for detected, non-accurate result
    # cv2.rectangle(img, location, bottom_right, 255, line_thickness)
    # cv2.imshow('Match_clr', img)

    cv2.rectangle(img2, location, bottom_right, 255, line_thickness)
    cv2.imshow('Match_grey', img2)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()