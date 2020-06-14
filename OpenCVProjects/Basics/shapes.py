import cv2
import numpy as np

img = np.zeros([600, 600, 3], np.uint8)
img = cv2.line(img, (10,10), (10,500), (0,255,0), 7)
img = cv2.arrowedLine(img, (100,10), (30,500), (230,0,0), 7)
img = cv2.rectangle(img, (400,10), (200, 500), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'MICHAEL', (100,500), font, 4, (255,255,255), 6, cv2.LINE_AA)

cv2.imshow("STATUE", img)

cv2.waitKey(0)
cv2.destroyAllWindows()