import cv2
import numpy as np 

face_cascade = cv2.CascadeClassifier(r'C:\Users\t-mibenh\Desktop\studies\python\practice\CV\OpenCVProjects\Basics\im_env\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')

capture = cv2.VideoCapture(0)


while True:
    ret, frame = capture.read()

    face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)
    for (x, y, w, h) in face_rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
    cv2.imshow('Face Detector!', frame)

    c = cv2.waitKey(1)
    if c == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()   