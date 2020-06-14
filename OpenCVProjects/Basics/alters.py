import cv2
import numpy as np

img = cv2.imread(r"")
img2 = cv2.imread(r"")

print(img.shape)
print(img.size)
print(img.dtype)
print()

#(x,y,h,w) =cv2.selectROI(img)
#face = img[y:y+w, x:x+h]
#cv2.imshow("MEESSTYYYFACE", face)

'''b,g,r = cv2.split(img)
print(b,g,r)
img = cv2.merge((b, g, r))'''

img = cv2.resize(img, (512,512) )
img2 = cv2.resize(img2, (512,512) )

#dst = cv2.add(img2, img)
dst = cv2.addWeighted(img,.9,img2 ,.4,0)


cv2.imshow("MEESSTYYY", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()