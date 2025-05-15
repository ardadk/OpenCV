import random

import cv2 as cv
import numpy as np

src = cv.imread("qfai.jpg")

def process(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    corners = cv.goodFeaturesToTrack(gray,maxCorners=35,qualityLevel=0.05,minDistance=10)
    for pt in corners:
        print(pt)
        b = np.random.randint(0,256)
        g = np.random.randint(0,256)
        r = np.random.randint(0,256)
        x = int(pt[0][0])
        y = int(pt[0][1])
        cv.circle(image,(x,y),5,(int(b),int(g),int(r)),2)
    return image
result = process(src)
cv.imshow("result",result)
cv.waitKey(0)
