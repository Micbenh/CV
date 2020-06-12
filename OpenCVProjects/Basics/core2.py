import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

import cv2 

#image blending

shreklogopath = r'C:\Users\t-mibenh\Desktop\studies\python\practice\imagemanip\Manipulator\images\pic.PNG'
football = r'C:\Users\t-mibenh\Desktop\studies\python\practice\imagemanip\Manipulator\images\roi.jpg'

img1 = cv2.imread(shreklogopath)
img2 = cv2.imread(football)

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()