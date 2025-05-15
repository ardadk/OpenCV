import cv2 as cv  # OpenCV kütüphanesi, görüntü işleme işlemleri için kullanılır
import numpy as np  # NumPy kütüphanesi, matris işlemleri ve sayısal işlemler için kullanılır

# Orijinal görüntüyü okur
src = cv.imread("qfai.jpg")

# Orijinal görüntüyü ekranda gösterir
cv.imshow("src", src)

# Kullanıcıdan bir tuşa basması beklenir
cv.waitKey(0)

# Renkli görüntüyü gri tonlamalı görüntüye dönüştürür
# cv.cvtColor(src, code)
# src: Giriş görüntüsü (renkli görüntü)
# code: Dönüşüm türü (cv.COLOR_BGR2GRAY, BGR'den GRAY'e dönüştürme)
# BGR (Mavi, Yeşil, Kırmızı) formatındaki görüntü gri tonlamalı (tek kanal) görüntüye dönüştürülür.
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# İkili (binary) eşikleme işlemi uygulanır
# cv.threshold(src, thresh, maxval, type)
# src: Giriş görüntüsü (gri tonlamalı görüntü)
# thresh: Eşik değeri (otomatik Otsu yöntemi kullanıldığı için 0 verildi)
# maxval: Eşiklenen piksellerin alacağı maksimum değer (255)
# type: Eşikleme türü (cv.THRESH_BINARY | cv.THRESH_OTSU)
# Otsu yöntemi, optimal eşik değerini otomatik olarak belirler ve ikili eşikleme uygular.
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

# Orijinal görüntünün boyutlarını alır
# src.shape: (yükseklik, genişlik, kanal) şeklinde bir tuple döner
# [:2] ifadesi, bu tuple'dan yalnızca yükseklik (h) ve genişlik (w) değerlerini alır
h, w = src.shape[:2]

# İkili eşiklenmiş görüntüyü ekranda gösterir
cv.imshow("binary", binary)

# Kullanıcıdan bir tuşa basması beklenir
cv.waitKey(0)
