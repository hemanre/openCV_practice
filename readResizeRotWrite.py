import cv2

img = cv2.imread('assets/puppy.png', 1)
img = cv2.resize(img, (0, 0), fx=1, fy=1)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_puppy.png', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()