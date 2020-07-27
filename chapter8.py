import cv2
import numpy as np


def getContours(img):
    countours, heirachy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in countours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 3)
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            num_corners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 0, 200), 2)
            if num_corners == 3:
                object_type = 'Triangle'
            elif num_corners == 4:
                object_type = 'Rectangle'
            elif num_corners == 6:
                object_type = 'hexagon'
            elif num_corners > 6:
                object_type = 'Circle'
            else:
                object_type = 'notTriangle'
            cv2.putText(imgContour, object_type, (x, y + h), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 0), 1)


path = 'resources/shapes.png'
img = cv2.imread(path)

# success, vid = img.read()

# img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
imgContour = img.copy()
cv2.imshow('img', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (9, 9), 2)
img = cv2.Canny(img, 30, 20)
cv2.imshow('cann', img)
getContours(img)
# cv2.imshow('shapes', img)
cv2.imshow('cont', imgContour)
cv2.waitKey(0)
