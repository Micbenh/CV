import cv2
import numpy as np

face_cascad = cv2.CascadeClassifier(r'C:\Users\t-mibenh\Desktop\studies\python\practice\CV\OpenCVProjects\Basics\im_env\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')

#mask init
face_mask = cv2.imread(r'C:\Users\t-mibenh\Desktop\studies\python\practice\CV\OpenCVProjects\Video\images\hannibal.png')
mask_h, mask_w = face_mask.shape[:2]

if face_cascad.empty():
    raise IOError("Unable to load face cascade clasifer xml file!")

capture = cv2.VideoCapture(0)
if not capture.isOpened():
    raise IOError("Webcam could not be accessed!")

while True:
    ret, frame = capture.read()

    face_rects = face_cascad.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)
    for (x, y, w, h) in face_rects:
        if h <= 0 or w <= 0: pass

        #adjust hieght and weight parameters
        h, w = int(1.0 * h), int(1.0 * w)
        y-= int(-0.2 * h)
        x = int(x)

        #extract region of intrest
        frame_roi = frame[y:y + h, x:x + w]
        face_mask_small = cv2.resize(face_mask, (w,h), interpolation = cv2.INTER_AREA)

        #convert mask to gray
        gray_mask = cv2.cvtColor(face_mask_small, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(gray_mask, 190, 255, cv2.THRESH_BINARY_INV)

        mask_inv = cv2.bitwise_not(mask)

        try:
            masked_face = cv2.bitwise_and(face_mask_small,face_mask_small ,mask=mask)
            masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv)
        except cv2.error as e:
                print('IGNORING ARTHIMETIC OPERATIONS')

        #add two imgaes together for final output
        frame[y:y+h, x:x+w] = cv2.add(masked_face, masked_frame)
    cv2.imshow('LOOK AT ME', frame)

    c = cv2.waitKey(1)
    if c == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()