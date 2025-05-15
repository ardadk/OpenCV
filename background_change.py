import cv2 as cv  # OpenCV kütüphanesi, görüntü işleme işlemleri için kullanılır
import numpy as np  # NumPy kütüphanesi, matris işlemleri ve sayısal işlemler için kullanılır

# Orijinal görüntüyü okur ve %50 boyutuna küçültür
src = cv.imread("qfai.jpg")
src = cv.resize(src, (0, 0), fx=0.5, fy=0.5)

# Kullanıcıya görüntü üzerinde bölge seçtiren araç
# Kullanıcı fare ile bir dikdörtgen çizer ve enter'a basar
r = cv.selectROI("input", src, False)

# Kullanıcı tarafından seçilen bölgeyi keser
roi = src[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

# Orijinal görüntünün bir kopyasını oluşturur
img = src.copy()

# Seçilen bölgeyi çerçeve içine alır (mavi dikdörtgen)
cv.rectangle(img, (int(r[0]), int(r[1])), (int(r[0]) + int(r[2]), int(r[1]) + int(r[3])), (255, 0, 0), 2)

# Maske oluşturur (aynı boyutta ve tek kanallı)
mask = np.zeros(src.shape[:2], dtype=np.uint8)

# Kullanıcı tarafından seçilen bölgenin koordinatları
rect = (int(r[0]), int(r[1]), int(r[2]), int(r[3]))

# Arka plan ve ön plan modellerini başlatır
bgdmodel = np.zeros((1, 65), np.float64)
fgdmodel = np.zeros((1, 65), np.float64)

# GrabCut algoritmasını çalıştırır
# Bu işlem, nesneyi arka plandan ayırmaya çalışır
cv.grabCut(src, mask, rect, bgdmodel, fgdmodel, 11, mode=cv.GC_INIT_WITH_RECT)

# Maske değerlerini 0 ve 1'e dönüştürerek 255 ile çarpar
# 1 ve 3 değerine sahip pikseller ön plandaki nesneleri temsil eder
mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype("uint8")

# Arka plan görüntüsünü okur
background = cv.imread("a.jpg")

# Arka plan görüntüsünü orijinal görüntüyle aynı boyuta getirir
h, w, ch = src.shape
background = cv.resize(background, (w, h))

# İkinci bir maske oluşturur
mask = np.zeros(src.shape[:2], dtype=np.uint8)

# Arka plan ve ön plan modellerini başlatır (tekrar)
bgdmodel = np.zeros((1, 65), np.float64)
fgdmodel = np.zeros((1, 65), np.float64)

# GrabCut algoritmasını tekrar çalıştırır
# Daha fazla iterasyon (5) kullanılarak daha iyi bir sonuç elde edilir
cv.grabCut(src, mask, rect, bgdmodel, fgdmodel, 5, mode=cv.GC_INIT_WITH_RECT)

# Maske değerlerini 0 ve 1'e dönüştürerek 255 ile çarpar
# 1 ve 3 değerine sahip pikseller ön plandaki nesneleri temsil eder
mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype("uint8")

# Yapısal eleman oluşturur (3x3 dikdörtgen)
se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))

# Morfolojik genişletme (dilate) işlemi yapar
# Bu, maskenin daha kalın olmasını sağlar, küçük boşlukları doldurur
cv.dilate(mask2, se, mask2)

# Maskeye Gauss bulanıklaştırma uygular
# Bu, maskeyi daha yumuşak hale getirir ve geçişlerin daha pürüzsüz olmasını sağlar
mask2 = cv.GaussianBlur(mask2, (5, 5), 0)

# Arka plan görüntüsünü de yumuşatır (bulanıklaştırır)
# Bu, arka plandaki keskinliği kaldırarak daha doğal bir geçiş sağlar
background = cv.GaussianBlur(background, (0, 0), 15)

# Maskeyi normalize eder (0 ile 1 arasında değerler alacak şekilde)
mask2 = mask2 / 255.0

# Maskeyi 3 kanala genişletir (renkli görüntü ile çarpmak için)
a = mask2[..., None]

# Sonucu oluşturur
# Her bir pikselde src ve background arasında ağırlıklı ortalama hesaplanır
# src: Orijinal görüntü (ön plan)
# background: Arka plan görüntüsü
# a: Maske (0 ile 1 arasında değer alır)
# Formül: result = a * src + (1 - a) * background
result = a * (src.astype(np.float32)) + (1 - a) * (background.astype(np.float32))

# Sonucu ekranda gösterir
cv.imshow("result", result.astype(np.uint8))

# Kullanıcıdan bir tuşa basmasını bekler
cv.waitKey(0)
