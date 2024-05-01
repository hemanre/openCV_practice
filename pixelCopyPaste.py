import cv2
import random

img = cv2.imread('assets/puppy.png', -1)

#print 325st row of image
print(img[325]) #[255...] white pixel
#
print(img[325][45:300]) # random columns show different values

# Get the height, width, and number of channels of the image
height, width, channels = img.shape

print('h:{}, w:{}, c:{}'.format(height, width, channels))

# 1. Change first 50 rows to random pixels
for i in range(50):
	for j in range(width):
		# img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
		rgba = [random.randint(0, 255) for _ in range(4)]
		img[i, j] = rgba

# 2 Copy part of image and paste it inside the main image
tag = img[100:200, 200:400] # the rows and columns to copy - in that order
img[50:150, 0:200] = tag
		
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()