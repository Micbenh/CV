import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

import cv2 

football_path = r'C:\Users\t-mibenh\Desktop\studies\python\practice\imagemanip\Manipulator\images\roi.jpg'

#display original image
img = cv2.imread(football_path)
cv2.imshow("image",img)
cv2.waitKey()

#display gray image
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image",gray_image)
cv2.waitKey()

#show side by side
fig,ax = plt.subplots(1, 2, figsize=(15,12))
ax[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax[0].set_title("Original")

ax[1].imshow(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB))
ax[1].set_title("Grayscale")


plt.show()
