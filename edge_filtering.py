# FAST IMAGE EDGE FILTERING
# edgePreservingFilter kullanılarak görüntünün kenarları korunarak filtreleme yapılır.

import cv2 as cv  # OpenCV kütüphanesi, görüntü işleme işlemleri için kullanılır
import numpy as np  # NumPy kütüphanesi, matris işlemleri ve sayısal işlemler için kullanılır


src = cv.imread("a.jpg")


cv.imshow("input", src)


cv.waitKey(0)

# Orijinal görüntünün boyutlarını alır
# src.shape: (yükseklik, genişlik, kanal) şeklinde bir tuple döner
# [:2] ifadesi, bu tuple'dan yalnızca yükseklik (h) ve genişlik (w) değerlerini alır
h, w = src.shape[:2]

# edgePreservingFilter kullanılarak görüntünün kenarları korunarak filtreleme yapılır
# cv.edgePreservingFilter(src, flags, sigma_s, sigma_r)
# src: Filtre uygulanacak giriş görüntüsü
# flags: Kenar koruma filtresi türünü belirler.
#    - cv.RECURS_FILTER: Tekrarlamalı kenar koruma filtresi kullanılır.
#    - cv.NORMCONV_FILTER: Normallendirilmiş konvolüsyon filtresi kullanılır.
# sigma_s: Görüntüdeki kenar koruma seviyesini belirler.
#    - Daha büyük sigma_s değerleri, daha geniş bir komşuluk üzerinde etki eder.
# sigma_r: Parlaklık farkı eşiğini belirler.
#    - Daha küçük sigma_r değerleri, daha belirgin kenarların korunmasını sağlar.
dst = cv.edgePreservingFilter(src, sigma_s=100, sigma_r=0.4, flags=cv.RECURS_FILTER)

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

# Sonuç görüntüsünü yeniden boyutlandırır
# cv.resize(src, dsize, fx, fy, interpolation)
# src: Giriş görüntüsü
# dsize: Yeni boyut (genişlik, yükseklik) olarak belirtilir.
# w: Orijinal genişlik korunur.
# h//2: Yükseklik yarıya düşürülür (görüntünün yüksekliği küçültülmüş olur).
result = cv.resize(result, (w, h // 2))

# Yan yana eklenmiş görüntüyü ekranda gösterir
cv.imshow("result", result)


cv.waitKey(0)
