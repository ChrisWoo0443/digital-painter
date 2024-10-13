import cv2
import numpy as py

import cv2
import numpy as np

img = cv2.VideoCapture(1)
frameWidth = 1920
frameHeight = 1080

img.set(3, frameWidth)
img.set(4, frameHeight)
img.set(10,150)
def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", frameWidth, frameHeight)
cv2.createTrackbar("Hue min", "HSV", 0, 179, empty)
cv2.createTrackbar("Hue max", "HSV", 179, 179, empty)
cv2.createTrackbar("Saturation min", "HSV", 0, 255, empty)
cv2.createTrackbar("Saturation max", "HSV", 255, 255, empty)
cv2.createTrackbar("Value min", "HSV", 0, 255, empty)
cv2.createTrackbar("Value max", "HSV", 255, 255, empty)

while True:
    success, frame = img.read()
    flipped = cv2.flip(frame, 1)

    imgHSV = cv2.cvtColor(flipped, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue min", "HSV")
    h_max = cv2.getTrackbarPos("Hue max", "HSV")
    s_min = cv2.getTrackbarPos("Saturation min", "HSV")
    s_max = cv2.getTrackbarPos("Saturation max", "HSV")
    v_min = cv2.getTrackbarPos("Value min", "HSV")
    v_max = cv2.getTrackbarPos("Value max", "HSV")
    # print(h_min, h_max, s_min, s_max, v_min, v_max)



    cv2.imshow('frame', flipped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

