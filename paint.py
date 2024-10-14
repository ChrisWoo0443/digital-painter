import cv2
import numpy as np

img = cv2.VideoCapture(2)
frameWidth = 1920
frameHeight = 1080
img.set(3, frameWidth)
img.set(4, frameHeight)
img.set(10, 150)


myColors = [[41, 57, 55, 255, 99, 255], [80, 106, 33, 160, 0, 255]]

myColorsValue = [[245, 227, 66], [144, 245, 66]]

myPoints =[]


def get_contours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 500:
            perimeter = cv2.arcLength(i,True)
            approximate = cv2.approxPolyDP(i,0.01*perimeter,True)
            x, y, w, h = cv2.boundingRect(approximate)
    return x+w//2, y

def get_colors(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoint = []

    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = get_contours(mask)
        cv2.circle(imgResults, (x, y), 15, myColorsValue[count], cv2.FILLED)

        if x != 0 and y != 0:
            newPoint.append((x,y, count))
        count += 1

    return newPoint


def draw_on_canvas(myPoints, myColorsValue):
    for points in myPoints:
        cv2.circle(imgResults, (points[0], points[1]), 10, myColorsValue[points[2]], cv2.FILLED)


while True:
    success, frame = img.read()
    flipped = cv2.flip(frame, 1)

    imgResults = flipped.copy()
    newPoints = get_colors(flipped, myColors, myColorsValue)
    if len(newPoints) != 0:
        for point in newPoints:
            myPoints.append(point)
    if len(myPoints) != 0:
        draw_on_canvas(myPoints, myColorsValue)

    cv2.imshow('Painter', imgResults)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
