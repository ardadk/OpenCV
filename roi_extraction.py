import numpy as np  # NumPy kütüphanesi, matris işlemleri ve sayısal işlemler için kullanılır
import cv2 as cv  # OpenCV kütüphanesi, görüntü işleme işlemleri için kullanılır

# Video dosyasını okur
# cv.VideoCapture(filename)
# filename: Okunacak video dosyasının adı ("a.mp4")
cap = cv.VideoCapture("a.mp4")

# Arka plan çıkartıcıyı oluşturur
# cv.createBackgroundSubtractorMOG2(history, varThreshold)
# history: Arka plan modelinin öğrenileceği çerçeve sayısı (500 çerçeve)
# varThreshold: Arka plan modeli ile piksel arasındaki fark eşiği (100)
fgbg = cv.createBackgroundSubtractorMOG2(history=500, varThreshold=100)

# Video çerçevesi üzerinde işlem yapar
def process(image):
    # Arka plan çıkartıcıya giriş görüntüsünü uygular
    # fgbg.apply(image)
    # image: Arka plan modeliyle karşılaştırılacak giriş görüntüsü
    mask = fgbg.apply(image)

    # Morfolojik dönüşüm için yapısal bir eleman oluşturur
    # cv.getStructuringElement(shape, ksize, anchor)
    # shape: Elemanın şekli (cv.MORPH_RECT dikdörtgen)
    # ksize: Yapısal elemanın boyutu (1x5 boyutunda bir dikdörtgen)
    # anchor: Sabit noktayı belirler (-1, -1 ile merkez alınır)
    line = cv.getStructuringElement(cv.MORPH_RECT, (1, 5), (-1, -1))

    # Morfolojik açma işlemini uygular (gürültüyü kaldırır)
    # cv.morphologyEx(src, op, kernel)
    # src: Giriş görüntüsü (mask)
    # op: Uygulanacak morfolojik işlem türü (cv.MORPH_OPEN, açma işlemi)
    # kernel: Kullanılacak yapısal eleman (line)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, line)

    # Maske görüntüsünü ekranda gösterir
    cv.imshow("mask", mask)

    # Konturları bulur
    # cv.findContours(image, mode, method)
    # image: Kontur bulma işlemi yapılacak görüntü (mask)
    # mode: Konturların hiyerarşisini belirler (cv.RETR_EXTERNAL, dış konturlar)
    # method: Kontur yaklaşımı türü (cv.CHAIN_APPROX_SIMPLE, köşe noktaları tutulur)
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Her kontur üzerinde döner
    for c in range(len(contours)):
        # Kontur alanını hesaplar
        # cv.contourArea(contour)
        # contour: Alanı hesaplanacak kontur
        area = cv.contourArea(contours[c])

        # Alanı 150 pikselden küçük olan konturları atlar
        if area < 150:
            continue

        # Konturun minimum çevreleyen dikdörtgenini bulur
        # cv.minAreaRect(contour)
        # contour: Dış çerçevesi bulunacak kontur
        # Bu fonksiyon, konturu çevreleyen en küçük döndürülmüş dikdörtgeni döndürür
        rect = cv.minAreaRect(contours[c])

        # Bulunan dikdörtgen üzerine bir elips çizer
        # cv.ellipse(image, box, color, thickness, lineType)
        # image: Elipsin çizileceği giriş görüntüsü (image)
        # box: Elipsin çevreleyen dikdörtgeni (rect)
        # color: Elipsin rengi (0, 255, 0) (yeşil)
        # thickness: Elipsin kalınlığı (2 piksel)
        # lineType: Çizgi türü (8-bit)
        cv.ellipse(image, rect, (0, 255, 0), 2, 8)

        # Dikdörtgenin merkezine bir daire çizer
        # cv.circle(image, center, radius, color, thickness, lineType, shift)
        # image: Dairenin çizileceği giriş görüntüsü (image)
        # center: Dairenin merkezi (dikdörtgenin merkezi)
        # radius: Dairenin yarıçapı (2 piksel)
        # color: Dairenin rengi (255, 0, 0) (mavi)
        # thickness: Dairenin kalınlığı (2 piksel)
        # lineType: Çizgi türü (8-bit)
        # shift: Kesin koordinatlar için bit kaydırma (0, kaydırma yok)
        cv.circle(image, (np.int32(rect[0][0]), np.int32(rect[0][1])), 2, (255, 0, 0), 2, 8, 0)

    # İşlenmiş görüntüyü döndürür
    return image


# Sonsuz bir döngü ile her çerçeve üzerinde işlem yapar
while True:
    # Video dosyasından bir kare okur
    # cap.read()
    # ret: Kare okuma durumunu döndürür (True veya False)
    # frame: Okunan kare (görüntü)
    ret, frame = cap.read()

    # Video sonuna ulaşıldıysa döngüyü kır
    if not ret:
        break

    # Giriş görüntüsünü ekranda gösterir
    cv.imshow("input", frame)

    # Giriş görüntüsünü işleyen process() fonksiyonunu çağırır
    result = process(frame)

    # İşlenmiş görüntüyü ekranda gösterir
    cv.imshow("result", result)

    # 50 milisaniye boyunca bir tuşa basılması beklenir
    # cv.waitKey(delay)
    # delay: Milisaniye cinsinden gecikme süresi (50 ms)
    # Klavyeden bir tuşa basılırsa tuşun ASCII kodunu döndürür
    k = cv.waitKey(50) & 0xff

    # 'Esc' tuşuna basılırsa (ASCII kodu 27), döngü sonlanır
    if k == 27:
        break
