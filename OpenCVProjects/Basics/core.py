import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

import cv2 as cv

shreklogopath = r'C:\Users\t-mibenh\Desktop\studies\python\practice\imagemanip\Manipulator\images\pic.PNG'

'''
img = cv.imread(shreklogopath)
cv.imshow("i", img)
cv.waitKey()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("i", gray)
cv.waitKey()'''

#acessing pixels
img = cv.imread(shreklogopath)
px = img[100,100]
print(px)
print()

#img shape - 'rows, columns, channels'
print("rows, columns, channgels:", img.shape)
print()

#numbers of pixels
print("num of pixels:", img.size)


#dtype
print("data type: ", img.dtype)


print()

#splitting and merging image channels
print("Splitting channels")
b, g, r = cv.split(img)
print("blue: ", b)
print("green: ", g)
print("red: ", r)
print()
print("Merging: ")
img = cv.merge((b,g,r))
print(img)


