import cv2 as cv  # OpenCV kütüphanesi, görüntü işleme işlemleri için kullanılır
import numpy as np  # NumPy kütüphanesi, matris işlemleri ve sayısal işlemler için kullanılır


src = cv.imread("a.jpg")


cv.imshow("a", src)

cv.waitKey(0)

# Orijinal görüntünün boyutlarını alır
# src.shape: (yükseklik, genişlik, kanal sayısı) şeklinde bir tuple döner
# [:2] ifadesi, bu tuple'dan yalnızca yükseklik (h) ve genişlik (w) değerlerini alır
h, w = src.shape[:2]

# Bilateral filtre uygular
# cv.bilateralFilter(src, d, sigmaColor, sigmaSpace)
# src: Filtre uygulanacak giriş görüntüsü (src)
# d: Filtre çekirdeğinin çapı (piksel biriminde). 0 verilirse otomatik hesaplanır.
# sigmaColor: Renk uzayındaki filtre parametresi. Daha büyük değerler, daha fazla renklerin birbirine karışmasını sağlar.
# sigmaSpace: Koordinat uzayındaki filtre parametresi. Daha büyük değerler, daha geniş bir komşulukta etki eder.
dst = cv.bilateralFilter(src, 0, 50, 10)


cv.imshow("dst", dst)


cv.waitKey(0)

# Sonuç görüntüsü için boş bir görüntü oluşturur
# np.zeros(shape, dtype)
# shape: Görüntünün boyutunu belirtir (h, w*2, 3)
#    - h: Yükseklik (orijinal görüntü ile aynı)
#    - w*2: Genişlik, çünkü orijinal ve filtrelenmiş görüntü yan yana yerleştirilecek (2 katı genişlikte)
#    - 3: Renk kanalları (BGR, 3 kanal)
# dtype: Veri tipi, orijinal görüntünün veri türüyle aynı yapılır (src.dtype)
result = np.zeros([h, w * 2, 3], dtype=src.dtype)

# Orijinal görüntüyü "result" matrisinin sol tarafına kopyalar
# result[y1:y2, x1:x2, :] → Görüntünün hangi bölgesine kopyalama yapılacağını belirtir
# 0:h → Yükseklik aralığı, tüm satırları kapsar
# 0:w → Genişlik aralığı, görüntünün ilk w kadar bölümüne (sol tarafa) kopyalanır
# src: Kopyalanacak görüntü
result[0:h, 0:w, :] = src

# Filtrelenmiş görüntüyü "result" matrisinin sağ tarafına kopyalar
# result[y1:y2, x1:x2, :] → Görüntünün hangi bölgesine kopyalama yapılacağını belirtir
# 0:h → Yükseklik aralığı, tüm satırları kapsar
# w:2*w → Genişlik aralığı, w'den 2*w'ye kadar olan alan (yani sağ taraf)
# dst: Kopyalanacak filtrelenmiş görüntü
result[0:h, w:2 * w, :] = dst


cv.imshow("result", result)
cv.waitKey(0)
