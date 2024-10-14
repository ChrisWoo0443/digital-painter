import cv2
import numpy as np

img = cv2.VideoCapture(2)
frameWidth = 2560
frameHeight = 1440
img.set(3, frameWidth)
img.set(4, frameHeight)
img.set(10, 150)


myColors = [[80, 102, 15, 99, 148, 239], [34, 96, 7, 77, 0, 241]]  # blue

myColorsValue = [[0, 0, 0], [0, 0, 0]]  # blue[245, 227, 0]


myPoints = []


def get_contours(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 500:
            perimeter = cv2.arcLength(i, True)
            approximate = cv2.approxPolyDP(i, 0.02*perimeter, True)
            x, y, w, h = cv2.boundingRect(approximate)
    return x+w//2, y


def get_colors(image, my_colors, my_colors_value):
    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    count = 0
    new_point = []

    for color in my_colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(img_hsv, lower, upper)
        x, y = get_contours(mask)
        cv2.circle(imgResults, (x, y), 15, my_colors_value[count], cv2.FILLED)

        if x != 0 and y != 0:
            new_point.append([x, y, count])
        count += 1

    return new_point


def draw_on_canvas(my_points, my_color_value):
    for points in my_points:
        cv2.circle(imgResults, (points[0], points[1]), 20, my_color_value[points[2]], cv2.FILLED)


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
