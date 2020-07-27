import cv2
import numpy as np

# cam = cv2.VideoCapture(0)
# cam.set(3, 640)
# cam.set(4, 480)
#
# success = True
# while success:
#     success, img = cam.read()
#     imgcanny = cv2.Canny(img, 50, 100)
#     imgblur = cv2.Canny(img, 100, 100)
#     cv2.imshow('bluuuur', imgblur)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

kernel = np.array((1, 1), np.uint8)
img = cv2.imread('resources/shivam.jpg')
imgcanny = cv2.Canny(img, 100, 100)
erodedshivam = cv2.erode(imgcanny, kernel)
cv2.imshow('shivam', erodedshivam)

cv2.waitKey(0)