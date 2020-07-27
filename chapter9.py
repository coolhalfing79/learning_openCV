import cv2


faceCascade = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')
# shivam = cv2.imread('resources/shivam.jpg')
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
while True:
    success, img = cam.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.circle(img, (x + w // 2, y + h // 2 - h // 5), int(h//2.2), (255, 0, 0), 2)
        cv2.circle(img, (x+w//2, y+h//2+h//5), int(h//3), (255, 0, 0), 2)
        # cv2.minEnclosingTriangle(((x, y+h-h//5), (x+w, y+h-h//5), (x+w//2, y+h)))
    cv2.imshow('face', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
