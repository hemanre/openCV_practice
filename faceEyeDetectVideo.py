import numpy as np
import cv2

scaleFactor = 1.3 # low value = accurate but slow algorithm
minNeighbours = 6 # higher the value = less detections # quality factor
line_thickness = 2

# sample videos: https://github.com/intel-iot-devkit/sample-videos
# Docu: https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
# Ref: https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters
#cap = cv2.VideoCapture(0) # from Camera, increase number for more cameras in use
cap = cv2.VideoCapture('assets/head-pose-face.mp4') # capture
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor, minNeighbours)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), line_thickness)
        # region of interest for face is dependent on the face
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor, minNeighbours)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), line_thickness)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()