import cv2

# img = cv2.imread('resources/frosted glass.jpeg')
# cv2.imshow('output', img)
# cv2.waitKey(0)

cam = cv2.VideoCapture('resources/2020-07-26-145822.webm')

while True:
    success, img = cam.read()
    cv2.imshow('video', img)
    if cv2.waitKey(256) & 0xFF == ord('q'):
        break
