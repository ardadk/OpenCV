import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def custom_hist(gray):
    h, w = gray.shape  # Görüntünün yüksekliği (h) ve genişliği (w) alınır
    hist = np.zeros([256],
                    dtype=np.int32)  # 0-255 aralığında her pikselin frekansını tutan bir dizi oluşturulur (başlangıçta tüm değerler 0)

    # Tüm pikseller üzerinde gezinerek her pikselin parlaklık seviyesini hesaplar
    for row in range(h):  # Satırlar (yükseklik) boyunca döner
        for col in range(w):  # Sütunlar (genişlik) boyunca döner
            pv = gray[row, col]  # Mevcut pikselin parlaklık (0-255) değerini alır
            hist[pv] += 1  # Bu piksel değerinin karşılık geldiği dizideki değeri 1 artırır (parlaklık seviyesini sayar)

    y_pos = np.arange(0, 256, 1, dtype=np.int32)  # 0'dan 255'e kadar bir x ekseni dizisi oluşturur
    plt.bar(y_pos, hist, align="center", color="r", alpha=0.5)  # Histogramı çubuk grafik (bar plot) olarak çizer
    plt.xticks(y_pos, y_pos)  # X eksenine 0-255 arasındaki değerleri koyar
    plt.ylabel("Frequency")  # Y ekseninin etiketi (Frekans) olarak atanır
    plt.title("Histogram")  # Grafiğin başlığı atanır
    plt.show()  # Grafiği ekranda gösterir


def image_hist(image):
    cv.imshow("input", image)  # Orijinal görüntüyü ekranda gösterir
    color = ("blue", "green", "red")  # Görüntüdeki 3 kanalın isimleri ve renkleri
    for i, color in enumerate(color):  # BGR kanalları üzerinde sırayla döner
        # cv.calcHist(images, channels, mask, histSize, ranges)
        # images: Histogramı hesaplanacak görüntü
        # channels: Hangi kanal için histogram hesaplanacak (B=0, G=1, R=2)
        # mask: Tüm görüntüyü işlemek için None kullanılır
        # histSize: Histogramdaki aralıkların sayısı (0-255 arası için 256 aralık)
        # ranges: Piksel değer aralığı (0-256)
        hist = cv.calcHist([image], [i], None, [256], [0, 256])  # Belirli kanal için histogramı hesaplar

        # plt.plot(x, y, color='...') ile histogramı çizer
        plt.plot(hist, color=color)  # Mevcut kanalın histogramını çizer
        plt.xlim([0, 256])  # X eksenini 0 ile 255 arasında sınırlar

    plt.show()  # Grafiği ekranda gösterir

src = cv.imread("qfai.jpg")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)
cv.waitKey(0)

gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
custom_hist(gray)
image_hist(src)