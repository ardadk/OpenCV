import numpy as np
import cv2 as cv

img = cv.imread("qfai.jpg",cv.IMREAD_GRAYSCALE)

#minMaxLoc Methodu
#minimum ve maksimum değer image'in en küçük ve en büyük renk değerlerini temsil eder.
#min_loc min_value'nun koordinatını max_loc ise max_value'nun koordinatını temsil eder.
min_value, max_value,min_loc,max_loc = cv.minMaxLoc(img)
print("min_value : %.2f, max_value : %.2f" % (min_value,max_value))
print("min loc:",min_loc,",","max loc:",max_loc)

#meanStdDev Methodu
#piksellerdeki renk değerlerinin ortalamasını ve standart sapmasını hesaplar.
means,stddev = cv.meanStdDev(img)
print("mean : %.2f,stddev: %.2f" % (means,stddev))
                               #piksellerdeki renk değerleri;
img[np.where(img < means)] = 0 #ortalamanın altındaysa siyaha
img[np.where(img>means)] = 255 #üstündeyse beyaza çevir

cv.imshow("img",img)
cv.waitKey(0)
