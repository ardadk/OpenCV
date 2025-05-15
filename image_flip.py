import cv2 as cv
import numpy as np

img = cv.imread("sally.jpg")

#X Flip (X eksenine göre döndürme)
a = cv.flip(img,0) #0 parametresi x eksenini ifade eder

cv.imshow("img",a)
cv.waitKey(0)
#Y Flip (Y eksenine göre döndürme)
b = cv.flip(img,1) #1 parametresi y eksenini ifade eder
cv.imshow("img",b)
cv.waitKey(0)

#X-Y Flip (Hem X eksenine hem Y eksenine göre döndürme)
c = cv.flip(img,-1) #-1 parametresi her iki ekseni de ifade eder)
cv.imshow("img",c)
cv.waitKey(0)