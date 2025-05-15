import cv2 as cv
import numpy as np
path = "C:/Users/Arda/Desktop/OpenCV/"
# Görüntüleri yükleyin
img1 = cv.imread('mcqueen.jpg')
img2 = cv.imread('sally.jpg')

horizon =np.hstack((img1,img2)) #np.hstack methodu image'leri yatay eksende birleştirmeye yarar.
                                #Parametre olarak 2 image değişkeni alır. Birleştirme işleminde;
                                #ilk yazılan soldaki ikinci yazılan sağdaki image olur.
cv.imshow('horizon',horizon)
cv.waitKey(0)