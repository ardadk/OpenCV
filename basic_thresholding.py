import cv2 as cv
import numpy as np

src = cv.imread("qfai.jpg")
T = 127 #Eşikleme için kullanılan eşik değer
gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY) #gri tonlamaya çevirdik

for i in range(5):
    ret,binary = cv.threshold(gray,T,255,i)
    #ilk parametre eşikleme yapılacak image'i temsil eder.
    #ikinci parametre eşikleme değerini temsil eder.
    #3.parametre eşikleme sonucunda kullanılacak maksimum değeri temsil eder.255 için beyaz.
    #4.parametre eşikleme türünü belirler
    #EŞİKLEME TÜRLERİ
    # 0--->	cv.THRESH_BINARY (ikili eşikleme)
    # 1--->	cv.THRESH_BINARY_INV (ters ikili eşikleme)
    # 2--->	cv.THRESH_TRUNC (kesik eşikleme)
    # 3--->	cv.THRESH_TOZERO (sıfıra eşikleme)
    # 4--->	cv.THRESH_TOZERO_INV (ters sıfıra eşikleme)
    #Genel olarak thresholding işlemi bir eşik değeri üzerindeyse bu değeri ata altındaysa bu değeri ata mantığıyla çalışır.

    cv.imshow("binary"+str(i),binary)

cv.waitKey(0)