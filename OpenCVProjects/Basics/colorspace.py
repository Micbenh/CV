import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

import cv2 

football_path = r'C:\Users\t-mibenh\Desktop\studies\python\practice\imagemanip\Manipulator\images\roi.jpg'
img = cv2.imread(football_path)

hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

fix, ax = plt.subplots(2, 2, figsize=(15, 12))

ax[0][0].imshow(cv2.cvtColor(hsv_image, cv2.COLOR_BGR2RGB))
ax[0][0].set_title("HSV Image")

ax[0][1].imshow(cv2.cvtColor(hsv_image[: , :, 0], cv2.COLOR_BGR2RGB))
ax[0][1].set_title("Hue Channel")

ax[1][0].imshow(cv2.cvtColor(hsv_image[:, :, 1], cv2.COLOR_BGR2RGB))
ax[1][0].set_title("Saturation Channel")

ax[1][1].imshow(cv2.cvtColor(hsv_image[:, :, 2], cv2.COLOR_BGR2RGB))
ax[1][1].set_title("Value Channel")

plt.show()

cv2.imwrite('football_hsv_image.png', hsv_image)
cv2.imwrite('images\\football_Hue_Channel.png', hsv_image[:, :, 0])
cv2.imwrite('images\\football_Saturation_Channel.png', hsv_image[:, :, 1])
cv2.imwrite('images\\football_Value_Channel.png', hsv_image[:, :, 2])