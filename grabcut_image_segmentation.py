import cv2 as cv  # OpenCV kütüphanesi, görüntü işleme işlemleri için kullanılır
import numpy as np  # NumPy kütüphanesi, matris işlemleri ve sayısal işlemler için kullanılır

# Orijinal görüntüyü okur
# cv.imread(filename)
# filename: Yüklenecek resim dosyasının adı ("qfai.jpg")
src = cv.imread("qfai.jpg")

# Görüntünün boyutunu %50 küçültür
# cv.resize(src, dsize, fx, fy)
# src: Giriş görüntüsü
# dsize: Görüntünün yeni boyutu (kullanılmadı)
# fx, fy: Yatay ve dikey ölçek faktörleri (0.5, yani %50 küçültme)
src = cv.resize(src, (0, 0), fx=0.5, fy=0.5)

# Kullanıcıdan bölge seçmesini ister
# cv.selectROI(windowName, img, showCrosshair)
# windowName: Görüntüyü göstereceği pencerenin adı ("input")
# img: Bölge seçimi yapılacak giriş görüntüsü (src)
# showCrosshair: İmlecin merkezine bir artı işareti ekler (False, eklemez)
# r: Kullanıcının seçtiği dikdörtgenin koordinatları (x, y, w, h)
r = cv.selectROI("input", src, False)

# Kullanıcı tarafından seçilen ROI'yi (Region of Interest) keser
# Giriş görüntüsünden (src) kullanıcı tarafından seçilen bölgeyi alır
# r[0]: x koordinatı, r[1]: y koordinatı, r[2]: genişlik, r[3]: yükseklik
roi = src[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

# Orijinal görüntünün bir kopyasını oluşturur
img = src.copy()

# Seçilen bölgeyi bir dikdörtgen ile çizer
# cv.rectangle(image, pt1, pt2, color, thickness)
# image: Dikdörtgenin çizileceği görüntü (img)
# pt1: Dikdörtgenin sol üst köşesinin koordinatları (int(r[0]), int(r[1]))
# pt2: Dikdörtgenin sağ alt köşesinin koordinatları (int(r[0]) + int(r[2]), int(r[1]) + int(r[3]))
# color: Dikdörtgenin rengi (255, 0, 0) (BGR formatında mavi)
# thickness: Çizgi kalınlığı (2 piksel)
cv.rectangle(img, (int(r[0]), int(r[1])), (int(r[0]) + int(r[2]), int(r[1]) + int(r[3])), (255, 0, 0), 2)

# Maske oluşturur (aynı boyutta ve tek kanallı)
# np.zeros(shape, dtype)
# shape: Boyut (yükseklik, genişlik) (src.shape[:2])
# dtype: Veri türü (uint8)
mask = np.zeros(src.shape[:2], dtype=np.uint8)

# ROI'yi dikdörtgen koordinatları olarak kaydeder
# (x, y, w, h) şeklindeki dikdörtgeni tanımlar
rect = (int(r[0]), int(r[1]), int(r[2]), int(r[3]))

# Arka plan ve ön plan modellerini oluşturur
# np.zeros(shape, dtype)
# shape: Boyut (1, 65) (grabCut için gereklidir)
# dtype: Veri türü (np.float64)
bgdmodel = np.zeros((1, 65), np.float64)  # Arka plan modeli
fgdmodel = np.zeros((1, 65), np.float64)  # Ön plan modeli

# GrabCut algoritmasını uygular
# cv.grabCut(img, mask, rect, bgdModel, fgdModel, iterCount, mode)
# img: Giriş görüntüsü
# mask: Ön plan ve arka plan etiketlerini içeren maske
# rect: ROI'yi belirten dikdörtgen (x, y, w, h)
# bgdModel: Arka plan modeli (önceki çerçevede arka planı temsil eder)
# fgdModel: Ön plan modeli (önceki çerçevede ön planı temsil eder)
# iterCount: Algoritmanın çalışacağı iterasyon sayısı (11 iterasyon)
# mode: Başlatma modu (cv.GC_INIT_WITH_RECT, bir dikdörtgen ile başlat)
cv.grabCut(src, mask, rect, bgdmodel, fgdmodel, 11, mode=cv.GC_INIT_WITH_RECT)

# Maske değerlerini 0 ve 1'e dönüştürerek 255 ile çarpar
# np.where(condition, x, y)
# condition: Koşul ((mask == 1) + (mask == 3)), mask'in 1 (ön plan) ve 3 (muhtemel ön plan) olan kısımlarını seçer
# x: Koşul doğru olduğunda kullanılacak değer (255)
# y: Koşul yanlış olduğunda kullanılacak değer (0)
# Bu işlem, maskede 1 ve 3 değerlerinin olduğu yerleri 255, diğer yerleri 0 yapar.
mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype("uint8")

# Bitwise AND işlemini uygular
# cv.bitwise_and(src1, src2, mask)
# src1: Birinci giriş görüntüsü (src)
# src2: İkinci giriş görüntüsü (src)
# mask: Maske görüntüsü (mask2)
# Bu işlem, mask2'deki 255 olan piksellerin karşılık geldiği src piksellerini kopyalar.
result = cv.bitwise_and(src, src, mask=mask2)

# Seçilen bölgeyi ekranda gösterir
cv.imshow("roi", roi)

# Sonuç görüntüsünü ekranda gösterir
cv.imshow("result", result)
