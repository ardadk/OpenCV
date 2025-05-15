import cv2 as cv  # OpenCV kütüphanesi, görüntü işleme işlemleri için kullanılır
import numpy as np  # NumPy kütüphanesi, matris işlemleri ve sayısal işlemler için kullanılır

# Orijinal görüntüyü okur
src = cv.imread("a.jpg")

# Orijinal görüntünün boyutlarını alır
# src.shape: (yükseklik, genişlik, kanal) şeklinde bir tuple döner
# [:2] ifadesi, bu tuple'dan yalnızca yükseklik (h) ve genişlik (w) değerlerini alır
h, w = src.shape[:2]

# X yönündeki (yatay) gradyanı hesaplar
# cv.Sobel(src, ddepth, dx, dy, ksize)
# src: Gradyanı hesaplanacak giriş görüntüsü
# ddepth: Çıkış görüntüsünün derinliğini belirtir (cv.CV_32F: 32 bit kayan nokta)
# dx: x yönünde türev derecesi (1 olduğu için x yönünde türev alınır)
# dy: y yönünde türev derecesi (0 olduğu için y yönünde türev alınmaz)
# ksize: Çekirdek boyutu (varsayılan değeri 3)
x_grad = cv.Sobel(src, cv.CV_32F, 1, 0)

# Y yönündeki (dikey) gradyanı hesaplar
# cv.Sobel(src, ddepth, dx, dy, ksize)
# src: Gradyanı hesaplanacak giriş görüntüsü
# ddepth: Çıkış görüntüsünün derinliğini belirtir (cv.CV_32F: 32 bit kayan nokta)
# dx: x yönünde türev derecesi (0 olduğu için x yönünde türev alınmaz)
# dy: y yönünde türev derecesi (1 olduğu için y yönünde türev alınır)
# ksize: Çekirdek boyutu (varsayılan değeri 3)
y_grad = cv.Sobel(src, cv.CV_32F, 0, 1)

# Mutlak değer almaya yarar
# x_grad'ı 8 bit tamsayıya (0-255) dönüştürür
# cv.convertScaleAbs(src)
# src: Giriş görüntüsü (32F formatında kayan nokta değeri)
# Bu işlem, her piksel değerini |src| değerine dönüştürür ve ardından 8-bit'e ölçekler.
x_grad = cv.convertScaleAbs(x_grad)

# Mutlak değer almaya yarar
# y_grad'ı 8 bit tamsayıya (0-255) dönüştürür
# cv.convertScaleAbs(src)
# src: Giriş görüntüsü (32F formatında kayan nokta değeri)
# Bu işlem, her piksel değerini |src| değerine dönüştürür ve ardından 8-bit'e ölçekler.
y_grad = cv.convertScaleAbs(y_grad)

# x gradyanını ekranda gösterir
cv.imshow("x_grad", x_grad)

# Kullanıcıdan bir tuşa basması beklenir
cv.waitKey(0)

# y gradyanını ekranda gösterir
cv.imshow("y_grad", y_grad)

# Kullanıcıdan bir tuşa basması beklenir
cv.waitKey(0)

# X ve Y gradyanlarını birleştirir
# cv.add(src1, src2, dst, mask, dtype)
# src1: Birinci giriş görüntüsü (x_grad)
# src2: İkinci giriş görüntüsü (y_grad)
# dtype: Çıktı görüntüsünün veri türü (cv.CV_16S), 16-bit tamsayıya kadar taşma olasılığını önlemek için kullanılır
# Gradyan büyüklüğünü almak için x_grad ve y_grad değerleri eklenir.
dst = cv.add(x_grad, y_grad, dtype=cv.CV_16S)

# Gradyan büyüklüğü görüntüsünü 8-bit tamsayıya dönüştürür
# cv.convertScaleAbs(src)
# src: Giriş görüntüsü (16-bit tamsayı)
# Her piksel değerini |src| değerine dönüştürür ve ardından 8-bit'e ölçekler.
dst = cv.convertScaleAbs(dst)

# x ve y gradyanlarının birleşimini ekranda gösterir
cv.imshow("gradient", dst)

# Kullanıcıdan bir tuşa basması beklenir
cv.waitKey(0)
