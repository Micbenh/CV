import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

import cv2

shreklogopath = r''

def viz_image():
    img = cv2.imread(shreklogopath)
    cv2.imshow("imaeg", img)
    cv2.waitKey()
    

def viz_gray_image():
    img = cv2.imread(shreklogopath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("image", gray)
    cv2.waitKey()

def viz_soblex_image():
    img = cv2.imread(shreklogopath)  
    sobelx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    cv2.imshow("image", sobelx)
    cv2.waitKey()
        
#viz_image()
#viz_gray_image()
#viz_soblex_image()