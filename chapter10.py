import cv2
import numpy as np

colors = [[0, 18, 122, 255, 255, 255]]


def getColorMaskedImage(image, colorslist):
    result = np.ones_like(image)
    imghsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    for color in colorslist:
        lower = np.array(color[0:3])
        higher = np.array(color[3:6])
        mask = cv2.inRange(imghsv, lower, higher)
        result = cv2.bitwise_and(img, img, mask=mask)
    return result


def createContour(image):
    pass


cam = cv2.VideoCapture(0)
cam.set(3, 480)
cam.set(4, 320)
while True:
    success, img = cam.read()
    cv2.imshow('img', img)
    maskedImage = getColorMaskedImage(img, colors)
    cv2.imshow('out', maskedImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
