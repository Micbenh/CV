import cv2
import numpy as np

img1 = np.zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img1, (200,0),(300,100), (255,255,255),-1)
img2 = np.zeros((250,500,3), np.uint8)
img2 = cv2.rectangle(img2, (50,0), (150,125), (255,255,255),-1)


#bitAnd = cv2.bitwise_and(img2,img1)
#bitOr = cv2.bitwise_or(img2, img1)
bitXOR = cv2.bitwise_xor(img2, img1)

cv2.imshow('img1', img1)
cv2.imshow("img2",img2)
#cv2.imshow("AND",bitAnd)
#cv2.imshow("Or",bitOr)
cv2.imshow("XOR",bitXOR)

cv2.waitKey(0)
cv2.destroyAllWindows()