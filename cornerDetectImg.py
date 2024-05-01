import numpy as np
import cv2

width_shrink_factor = 0.75
height_shrink_factor = 0.75

num_good_corners = 10
min_quality_factor = 0.01
min_distance_between_corners = 10 # euclidean distance

radius = 5

img = cv2.imread('assets/chessboard.png')
img = cv2.resize(img, (0, 0), fx=width_shrink_factor, fy=height_shrink_factor)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale to facilitate detection

# Shi Tomashi corner detection: https://docs.opencv.org/4.x/d4/d8c/tutorial_py_shi_tomasi.html

corners = cv2.goodFeaturesToTrack(gray, num_good_corners, min_quality_factor, min_distance_between_corners)
# print(corners) # float
corners = np.int0(corners)

for corner in corners:
	x, y = corner.ravel() # [[x,y]] -> [x,y]
	cv2.circle(img, (x, y), radius, (255, 0, 0), -1) # Draw corners on the original image

for i in range(len(corners)):
	for j in range(i + 1, len(corners)):
		corner1 = tuple(corners[i][0])
		corner2 = tuple(corners[j][0])
		color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3))) # randint gives 64 bit integer. This is converted to regular python datatype int.
		cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()