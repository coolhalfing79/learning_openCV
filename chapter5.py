import cv2
import numpy as np


def empty(n):
    pass


path = 'resources/shivam.jpg'
cv2.namedWindow('trackWin')
cv2.createTrackbar('hue-min', 'trackWin', 0, 179, empty)
cv2.createTrackbar('hue-max', 'trackWin', 255, 255, empty)
cv2.createTrackbar('sat-min', 'trackWin', 18, 179, empty)
cv2.createTrackbar('sat-max', 'trackWin', 255, 255, empty)
cv2.createTrackbar('val-min', 'trackWin', 122, 179, empty)
cv2.createTrackbar('val-max', 'trackWin', 255, 255, empty)

while True:
    img = cv2.imread(path)
    # img = cv2.resize(img, (1024//2, 786//2))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("hue-min", "trackWin")
    h_max = cv2.getTrackbarPos("hue-max", "trackWin")
    s_min = cv2.getTrackbarPos("sat-min", "trackWin")
    s_max = cv2.getTrackbarPos("sat-max", "trackWin")
    v_min = cv2.getTrackbarPos("val-min", "trackWin")
    v_max = cv2.getTrackbarPos("val-max", "trackWin")
    # print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    higher = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, higher)
    cv2.imshow("image", img)
    # cv2.imshow("HSVimg", imgHSV)
    # cv2.imshow('mask', mask)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('result', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
