import cv2
import numpy as np


img = np.zeros((600, 800, 3), np.uint8)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 255, 255), 1)
cv2.rectangle(img, (0, 0), (256, 256), (255, 255, 255), cv2.FILLED)
cv2.circle(img, (img.shape[1]//2, img.shape[0]//2), 50, (255, 0, 255), 2)
cv2.putText(img, 'open sim sim', (400, 100), cv2.FONT_HERSHEY_PLAIN, 2, (150, 0, 150), 3)
cv2.imshow('image', img)
cv2.waitKey(0)