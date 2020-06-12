import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

import cv2

football_path = r'C:\Users\t-mibenh\Desktop\studies\python\practice\imagemanip\Manipulator\images\roi.jpg'

img = cv2.imread(football_path)

#cutting
print(img.shape)
print(img.shape[:2])

#extracting size from shape
height, width = img.shape[:2]

#choosing croping x and y
start_row, start_col = int(height * 0.25), int(width * 0.25)
end_row, end_col =  int(height * 0.75), int(width * 0.75)

#applying crop
crop = img[start_row:end_row, start_col:end_col]

#blur image
blurred = cv2.GaussianBlur(img, (13, 13), 3)

#edge detection
canny = cv2.Canny(img, 120, 360)


#display
fix,ax =  plt.subplots(2, 2, figsize=(15, 12))

ax[0][0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax[0][0].set_title("Original image")

ax[0][1].imshow(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
ax[0][1].set_title('Cropped image')

ax[1][0].imshow(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
ax[1][0].set_title("Blured Image")

ax[1][1].imshow(cv2.cvtColor(canny, cv2.COLOR_BGR2RGB))
ax[1][1].set_title("Edge Detection Image")

plt.show()