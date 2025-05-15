import cv2 as cv  # OpenCV kütüphanesi, görüntü işleme işlemleri için kullanılır
import numpy as np  # NumPy kütüphanesi, matris işlemleri ve sayısal işlemler için kullanılır

# Orijinal görüntüyü okur
src = cv.imread("a.jpg")

# Orijinal görüntüyü ekranda gösterir
cv.imshow("keanu", src)

# Kullanıcıdan bir tuşa basması beklenir
cv.waitKey(0)

# Canny kenar tespiti uygulanır
# cv.Canny(image, threshold1, threshold2)
# image: Giriş görüntüsü
# threshold1: Alt eşik değeri, kenar tespiti için minimum gradyan büyüklüğü
# threshold2: Üst eşik değeri, kenar tespiti için maksimum gradyan büyüklüğü
# Görüntüdeki kenarların belirlenmesi için alt eşik 100, üst eşik 300 olarak ayarlanmıştır.
edge = cv.Canny(src, 100, 300)

# Canny kenar tespiti sonucu görüntüyü ekranda gösterir
cv.imshow("mask image", edge)

# Kullanıcıdan bir tuşa basması beklenir
cv.waitKey(0)
