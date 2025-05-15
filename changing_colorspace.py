import cv2 as cv

#HSV renk uzayı

img = cv.imread("qfai.jpg")
cv.namedWindow("rgb",cv.WINDOW_AUTOSIZE)
cv.imshow("rgb",img)
cv.waitKey(0)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(0)

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsw",hsv)
cv.waitKey(0)
cv.destroyAllWindows()