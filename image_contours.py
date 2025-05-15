import cv2 as cv  # OpenCV kütüphanesi, görüntü işleme işlemleri için kullanılır

# İkili eşikleme (binary threshold) işlemini gerçekleştirir
def threshold_demo(image):
    # Gaussian Blur filtresi uygular
    # cv.GaussianBlur(src, ksize, sigmaX)
    # src: Giriş görüntüsü
    # ksize: Çekirdek boyutu (3x3 boyutunda bulanıklaştırma çekirdeği)
    # sigmaX: X eksenindeki Gauss dağılımının standart sapması (0 ise otomatik hesaplanır)
    dst = cv.GaussianBlur(image, (3, 3), 0)

    # Renkli görüntüyü gri tonlamalı görüntüye dönüştürür
    # cv.cvtColor(src, code)
    # src: Giriş görüntüsü (BGR formatında)
    # code: Renk uzayı dönüşüm kodu (cv.COLOR_BGR2GRAY)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)

    # İkili eşikleme işlemi uygular
    # cv.threshold(src, thresh, maxval, type)
    # src: Giriş görüntüsü (gri tonlamalı)
    # thresh: Eşik değeri (Otsu yöntemi kullanıldığı için 0 verilir)
    # maxval: Eşikleme sonrası pikselin alacağı maksimum değer (255)
    # type: Eşikleme türü (Otsu yöntemi ve binary eşikleme birlikte kullanılır)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)

    # İkili eşiklenmiş görüntüyü ekranda gösterir
    cv.imshow("binary", binary)

    # İkili eşiklenmiş görüntüyü döndürür
    return binary


# Canny kenar tespiti işlemini gerçekleştirir
def canny_demo(image):
    # Canny kenar tespiti işlemi uygular
    # cv.Canny(image, threshold1, threshold2)
    # image: Giriş görüntüsü
    # threshold1: Kenar tespiti için alt eşik değeri
    # threshold2: Kenar tespiti için üst eşik değeri
    # Canny kenar tespiti için alt eşik değeri 100, üst eşik değeri 100 * 2 = 200 olarak ayarlanır
    t = 100
    canny_output = cv.Canny(image, t, t * 2)

    # Canny kenar tespiti sonucunu ekranda gösterir
    cv.imshow("canny", canny_output)

    # Canny kenar tespiti sonucunu döndürür
    return canny_output


# Orijinal görüntüyü okur
src = cv.imread("a.jpg")

# "input" adlı bir pencere oluşturur
# cv.namedWindow(winname, flags)
# winname: Pencerenin adı ("input")
# flags: Pencerenin nasıl oluşturulacağını belirtir (cv.WINDOW_AUTOSIZE pencere boyutunu görüntüye göre ayarlar)
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)

# Orijinal görüntüyü "input" adlı pencerede gösterir
cv.imshow("input", src)

# Kullanıcıdan bir tuşa basmasını bekler
cv.waitKey(0)

# İkili eşikleme işlemini gerçekleştirir
binary = threshold_demo(src)

# Canny kenar tespiti işlemini gerçekleştirir
canny = canny_demo(src)

# Kenarları belirlenen görüntüde kontur bulur
# cv.findContours(image, mode, method)
# image: Kontur bulma işlemi yapılacak görüntü (genellikle ikili eşiklenmiş veya Canny sonucu)
# mode: Konturların hiyerarşi türü (cv.RETR_TREE, tüm konturların hiyerarşisini çıkarır)
# method: Konturu tanımlama yöntemi (cv.CHAIN_APPROX_SIMPLE, yalnızca köşe noktaları tutar)
# contours: Bulunan tüm konturları bir liste olarak döndürür
# hierarchy: Konturların hiyerarşisini döndürür
contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Bulunan konturları görüntüye çizer
# for döngüsü ile tüm konturların üzerinden geçer
for c in range(len(contours)):
    # cv.drawContours(image, contours, contourIdx, color, thickness, lineType)
    # image: Konturun çizileceği giriş görüntüsü
    # contours: Konturların listesi
    # contourIdx: Hangi konturun çizileceği (burada c, her bir kontur için döngü)
    # color: Kontur çizgi rengi (0, 0, 255) BGR formatında kırmızı renk
    # thickness: Kontur çizgisinin kalınlığı (2 piksel)
    # lineType: Çizgi türü (8-bit çizgi)
    cv.drawContours(src, contours, c, (0, 0, 255), 2, 8)

# Konturların çizildiği görüntüyü ekranda gösterir
cv.imshow("contours-demo", src)

# Kullanıcıdan bir tuşa basmasını bekler
cv.waitKey(0)
