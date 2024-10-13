import cv2
import numpy as np

img = cv2.VideoCapture(1)
frameWidth = 1920
frameHeight = 1080
img.set(3, frameWidth)
img.set(4, frameHeight)
img.set(10, 150)


myColors = [[41, 57, 55, 255, 99, 255], [80, 106, 33, 160, 0, 255]]

myColorsValue = []
def getContours(img):



def getColors(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []

    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResults, (x, y), 15, myColorsValue[count], cv2.FILLED)

        if x != 0 and y != 0:
            newPoints.append((x,y, count))
        count += 1

    return newPoints


while True:
    success, frame = img.read()
    flipped = cv2.flip(frame, 1)

    cv2.imshow('frame', flipped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
