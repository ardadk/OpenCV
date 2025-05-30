import cv2 as cv
import numpy as np

src = cv.imread("qfai.jpg")
def process(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    corners = cv.goodFeaturesToTrack(gray,100,0.05,10)
    print(len(corners))
    for pt in corners:
        print(pt)
        b = np.random.random_integers(0,256)
        g = np.random.random_integers(0,256)
        r = np.random.random_integers(0,256)
        x = int(pt[0][0])
        y = int(pt[0][1])
        cv.circle(image,(x,y),5,(int(b),int(g),int(r)),2)


    win_Size = (3,3)
    zeroZone = (-1,-1)

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_COUNT,40,0.001)
    corners = cv.cornerSubPix(gray,corners,win_Size,zeroZone, criteria)

    for i in range(corners.shape[0]):
        print("--Refined Corner [",i,"] (",corners[i,0,0], ",",corners[i,0,1],")")
    return image

process(src)
cv.imshow("src",src)
cv.waitKey(0)
