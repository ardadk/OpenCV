import cv2 as cv  # OpenCV kütüphanesi, görüntü işleme işlemleri için kullanılır
import numpy as np  # NumPy kütüphanesi, matris işlemleri ve sayısal işlemler için kullanılır

# Canny kenar tespiti işlemini gerçekleştirir
def canny_demo(image):
    # Kenar tespiti için eşik değeri belirlenir
    t = 80
    # Canny kenar tespiti işlemi uygular
    # cv.Canny(image, threshold1, threshold2)
    # image: Giriş görüntüsü
    # threshold1: Kenar tespiti için alt eşik değeri
    # threshold2: Kenar tespiti için üst eşik değeri
    # Eşik değerleri 80 ve 160 olarak ayarlanır
    canny_output = cv.Canny(image, t, t * 2)
    # Canny çıktısını bir dosyaya kaydeder
    # cv.imwrite(filename, image)
    # filename: Dosya adı ("canny_output.png")
    # image: Kaydedilecek görüntü (canny_output)
    cv.imwrite("canny_output.png", canny_output)
    # Canny çıktısını döndürür
    return canny_output

# Orijinal görüntüyü okur
src = cv.imread("b.png")

# "input" adlı bir pencere oluşturur
# cv.namedWindow(winname, flags)
# winname: Pencerenin adı ("input")
# flags: Pencerenin nasıl oluşturulacağını belirtir (cv.WINDOW_AUTOSIZE pencere boyutunu görüntüye göre ayarlar)
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)

# Orijinal görüntüyü "input" adlı pencerede gösterir
cv.imshow("input", src)

# Kullanıcıdan bir tuşa basmasını bekler
cv.waitKey(0)

# Canny kenar tespiti işlemini gerçekleştirir
binary = canny_demo(src)

# Canny sonucu görüntüyü ekranda gösterir
cv.imshow("binary", binary)

# Kullanıcıdan bir tuşa basmasını bekler
cv.waitKey(0)

# Hough dönüşümü ile doğru tespiti işlemini gerçekleştirir
# cv.HoughLines(image, rho, theta, threshold, lines, srn, stn)
# image: Giriş görüntüsü (genellikle kenar tespiti sonucu)
# rho: ρ değeri, doğruların tespitinde çözünürlüğü belirler (1 piksel çözünürlük)
# theta: θ değeri, doğruların açısal çözünürlüğü (np.pi/180 = 1 derece)
# threshold: Doğru olarak kabul edilmesi için gereken minimum oy sayısı (150)
# lines: Bulunan doğruların saklanacağı liste (None)
# srn: Çok ölçekli çözünürlük aralığı (kullanılmadığı için 0 verildi)
# stn: Açısal çözünürlük (kullanılmadığı için 0 verildi)
lines = cv.HoughLines(binary, 1, np.pi / 180, 150, None, 0, 0)

# Eğer herhangi bir doğru tespit edildiyse bu döngü çalışır
if lines is not None:
    # Bulunan her bir doğruyu döngü ile çizer
    for i in range(0, len(lines)):
        # Doğrunun polar koordinatlarını alır
        rho = lines[i][0][0]  # ρ (doğrunun uzaklığı)
        theta = lines[i][0][1]  # θ (doğrunun açısı)

        # θ (açı) kullanılarak doğrunun eğimi ve kesişim noktaları hesaplanır
        a = np.cos(theta)  # θ'nın kosinüsü
        b = np.sin(theta)  # θ'nın sinüsü
        x0 = a * rho  # x ekseninde başlangıç noktası
        y0 = b * rho  # y ekseninde başlangıç noktası

        # Doğruyu ekranda uzatmak için iki uç nokta hesaplanır
        pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))  # Doğrunun bir ucu
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))  # Doğrunun diğer ucu

        # Doğruyu çizer
        # cv.line(image, pt1, pt2, color, thickness, lineType)
        # image: Doğrunun çizileceği giriş görüntüsü (src)
        # pt1: Doğrunun başlangıç noktası
        # pt2: Doğrunun bitiş noktası
        # color: Doğrunun rengi (0, 0, 255) (BGR formatında kırmızı)
        # thickness: Doğrunun kalınlığı (3 piksel)
        # lineType: Çizgi türü (cv.LINE_AA, anti-aliasing)
        cv.line(src, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)
