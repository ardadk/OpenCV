import cv2 as cv  # OpenCV kütüphanesi, görüntü işleme işlemleri için kullanılır
import numpy as np  # NumPy kütüphanesi, matris işlemleri ve sayısal işlemler için kullanılır

# Video dosyasını okur
# cv.VideoCapture(filename)
# filename: Okunacak video dosyasının adı ("a.mp4")
cap = cv.VideoCapture("a.mp4")

# Videodan ilk kareyi okur
# ret: Okuma başarılıysa True, aksi halde False
# frame1: Okunan ilk çerçeve (görüntü)
ret, frame1 = cap.read()

# İlk çerçeveyi gri tonlamalı görüntüye dönüştürür
# cv.cvtColor(src, code)
# src: Giriş görüntüsü (frame1)
# code: Renk uzayı dönüşüm kodu (cv.COLOR_BGR2GRAY)
prvs = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)

# HSV renk uzayına uygun bir boş görüntü oluşturur
# np.zeros_like(array)
# array: Boyutları ve veri türü alınacak referans matris (frame1)
hsv = np.zeros_like(frame1)

# HSV görüntüsünün doygunluk (saturation) bileşenini maksimum yapar (tüm pikseller 255)
# Bu, görselleştirme için parlak bir renk görünümü sağlar
hsv[..., 1] = 255


# Yoğun optik akış (dense optical flow) hesaplayan fonksiyon
def dense_opt_flow(hsv, prvs):
    while True:
        # Videodan bir sonraki kareyi okur
        ret, frame2 = cap.read()

        # Okuma başarısız olursa (video sonuna gelirse) döngüden çıkar
        if not ret:
            break

        # Yeni çerçeveyi gri tonlamalı görüntüye dönüştürür
        nextt = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)

        # Farneback yöntemi ile yoğun optik akış hesaplar
        # cv.calcOpticalFlowFarneback(prev, next, flow, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags)
        # prev: Önceki çerçevenin gri tonlamalı görüntüsü
        # next: Mevcut çerçevenin gri tonlamalı görüntüsü
        # flow: Akış vektörlerini içeren boş matris (None olarak verildi, otomatik oluşturulur)
        # pyr_scale: Piramit ölçek faktörü (0.5)
        # levels: Piramit seviyelerinin sayısı (3)
        # winsize: Ortalama penceresi boyutu (15)
        # iterations: Her piramit seviyesindeki maksimum iterasyon sayısı (3)
        # poly_n: Piksel komşuluklarının boyutu (5)
        # poly_sigma: Gaussian standard sapması (1.2)
        # flags: Optik akış hesaplama için ek bayraklar (0)
        flow = cv.calcOpticalFlowFarneback(prvs, nextt, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        # Akış vektörlerinin büyüklük (mag) ve yön (ang) bileşenlerini hesaplar
        # cv.cartToPolar(x, y)
        # x: x eksenindeki akış vektörleri (flow[..., 0])
        # y: y eksenindeki akış vektörleri (flow[..., 1])
        # mag: Vektör büyüklüğü (her bir pikseldeki vektör büyüklüğü)
        # ang: Vektör yönü (her bir pikseldeki vektörün yön açısı)
        mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])

        # HSV görüntüsünün hue (ton) bileşenini açıya göre günceller
        # HSV'de hue, 0-180 arasında bir değer olarak temsil edilir
        hsv[..., 0] = ang * 180 / np.pi / 2

        # Büyüklük değerlerini normalize ederek value (parlaklık) bileşenine atar
        # cv.normalize(src, dst, alpha, beta, norm_type)
        # src: Giriş görüntüsü (mag)
        # dst: Çıktı görüntüsü (None olarak verildi, otomatik oluşturulur)
        # alpha: Normalizasyonun minimum değeri (0)
        # beta: Normalizasyonun maksimum değeri (255)
        # norm_type: Normalizasyon türü (cv.NORM_MINMAX, min-max normalizasyonu)
        hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)

        # HSV görüntüsünü BGR renk uzayına dönüştürür
        # cv.cvtColor(src, code)
        # src: Giriş görüntüsü (HSV)
        # code: Renk uzayı dönüşüm kodu (cv.COLOR_HSV2BGR)
        bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

        # Optik akış görüntüsünü ekranda gösterir
        cv.imshow("frame2", bgr)

