import cv2
import numpy as np

img = cv2.VideoCapture(1)
frameWidth = 1920
frameHeight = 1080
img.set(3, frameWidth)
img.set(4, frameHeight)
img.set(10, 150)


myColors = [[41, 57, 55, 255, 99, 255], [80, 106, 33, 160, 0, 255]]

while True:
    success, frame = img.read()
    flipped = cv2.flip(frame, 1)

    cv2.imshow('frame', flipped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
