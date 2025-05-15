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

src = cv.imread("qfai.jpg")
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow("input",gray)
cv.waitKey(0)
custom_hist(gray)

dst = cv.equalizeHist(gray) #histogram eşitleme uygulandı(kontrast ayarı)
cv.imshow("eh",dst)
cv.waitKey(0)

custom_hist(dst)