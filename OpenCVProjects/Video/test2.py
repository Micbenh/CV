import cv2
import numpy as np

face_cascad = cv2.CascadeClassifier(r'')
cat_ears = cv2.imread(r'')

if face_cascad.empty():
    raise IOError("Could not load face classifier xml!")


capture = cv2.VideoCapture(0)
if not capture.isOpened():
    raise IOError("Could not access webcam video stream!")

while True:
    ret, frame = capture.read()

    face_rects = face_cascad.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)
    for (x, y, w, h) in face_rects:
        if h <= 0 or w <= 0: pass
        w = int(1.0 * w)
        h = int(1.0 * h)
        y-= int(.50 * h)
        x = int(x)

        frame_roi = frame[y : y+h, x : x+w]
        cat_ears_resized = cv2.resize(cat_ears, (h, w), interpolation = cv2.INTER_AREA)

        gray_cat_ears = cv2.cvtColor(cat_ears_resized, cv2.COLOR_BGR2GRAY)
        ret, ears = cv2.threshold(gray_cat_ears, 180, 255, cv2.THRESH_BINARY_INV)
        ears_inv = cv2.bitwise_not(ears)

        try:
            masked_ears = cv2.bitwise_and(cat_ears_resized,cat_ears_resized, mask=ears)
            masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=ears_inv)
        except cv2.error as e:
            print("ERRRORR")
        
        frame[y:y + h, x: x + w] = cv2.add(masked_ears, masked_frame)
        cv2.imshow("EARS", frame)


    c = cv2.waitKey(1)
    if c == ord('q'):
        break

capture.release()
cv2.destoryAllWIndows()