import cv2


img = cv2.imread('resources/josefin-sbovFdDUk3s-unsplash.jpg')
resizedimg = cv2.resize(img, (800, 600))
cv2.imshow('img', resizedimg)
cv2.waitKey(1000)
