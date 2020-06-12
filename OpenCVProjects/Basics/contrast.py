import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

import cv2
shreklogopath = r'C:\Users\t-mibenh\Desktop\studies\python\practice\imagemanip\Manipulator\images\pic.PNG'


def change_con_and_br():
    img = cv2.imread(shreklogopath)
    if img is None:
        print("Could not import image")
        exit(0)

    new_img = np.zeros(img.shape, img.dtype)   

    alpha = 1.0
    beta = 0

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            for z in range(img.shape[2]):
                new_img[x,y,z] = np.clip(alpha * img[x,y,z] + beta,0,255)

    cv2.imshow("Original", img)
    cv2.imshow("New Image", new_img)
    cv2.waitKey()




change_con_and_br()