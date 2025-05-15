import cv2 as cv
import numpy as np

# Shifting (Görüntünün kaydırılması)
img = cv.imread("qfai.jpg")

rows = img.shape[0]  # Resmin satır (yükseklik) sayısını alır
cols = img.shape[1]  # Resmin sütun (genişlik) sayısını alır

# Dönüşüm matrisini tanımlıyoruz.
# 1. satır [1, 0, 300]
#    - 1: x eksenine etkisi, 1 olduğu için x ekseni boyunca kaydırma yapılmaz, orijinal x değerleri korunur.
#    - 0: y eksenine etkisi, 0 olduğu için x koordinatlarına herhangi bir y ekseni kaydırması uygulanmaz.
#    - 300: x ekseninde 300 birimlik pozitif yönde kaydırma yapar.
#
# 2. satır [0, 1, 90]
#    - 0: x eksenine etkisi, 0 olduğu için y koordinatları x'yi etkilemez.
#    - 1: y eksenine etkisi, 1 olduğu için y ekseni boyunca kaydırma yapılmaz, orijinal y değerleri korunur.
#    - 90: y ekseninde 90 birimlik pozitif yönde kaydırma yapar.
M = np.float32([[1, 0, 300],  # x ekseni kaydırması
                [0, 1, 90]])  # y ekseni kaydırması

# Resmi belirtilen matris M'ye göre kaydırır ve yeni bir görüntü oluşturur
shifted = cv.warpAffine(img, M, (cols, rows))

cv.imshow("img", img)  # Orijinal resmi gösterir
cv.waitKey(0)  # Klavyeden bir tuşa basılana kadar bekler
cv.imshow("shifted", shifted)  # Kaydırılmış resmi gösterir
cv.waitKey(0)  # Klavyeden bir tuşa basılana kadar bekler

# Rotation (Görüntünün döndürülmesi)

# Dönüşüm matrisini oluşturur
# (cols/2, rows/2) resmin merkezi etrafında dönüş yapılmasını sağlar
# 90, döndürme açısı (derece cinsinden)
# 1, ölçek faktörüdür, yani boyutu değiştirmez
M = cv.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)

# Resmi belirtilen matris M'ye göre döndürür ve yeni bir görüntü oluşturur
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow("rotated", dst)  # Döndürülmüş resmi gösterir
cv.waitKey(0)  # Klavyeden bir tuşa basılana kadar bekler

# Scaling (Görüntünün yeniden boyutlandırılması)
# fx = 0.4, yatay eksende %40 oranında küçültme
# fy = 0.4, dikey eksende %40 oranında küçültme
# interpolation=cv.INTER_CUBIC, yeniden boyutlandırma sırasında kullanılan enterpolasyon yöntemi (daha yumuşak bir görüntü sağlar)
res = cv.resize(img, None, fx=0.4, fy=0.4, interpolation=cv.INTER_CUBIC)

cv.imshow("resized", res)  # Yeniden boyutlandırılmış resmi gösterir
cv.waitKey(0)  # Klavyeden bir tuşa basılana kadar bekler

# Küçük resim işlemleri
rows = res.shape[0]  # Yeniden boyutlandırılan resmin satır (yükseklik) sayısını alır
cols = res.shape[1]  # Yeniden boyutlandırılan resmin sütun (genişlik) sayısını alır

# Dönüşüm matrisini tanımlıyoruz.
# 1. satır [1, 0, 300]
#    - 1: x eksenine etkisi, 1 olduğu için x ekseni boyunca kaydırma yapılmaz, orijinal x değerleri korunur.
#    - 0: y eksenine etkisi, 0 olduğu için x koordinatlarına herhangi bir y ekseni kaydırması uygulanmaz.
#    - 300: x ekseninde 300 birimlik pozitif yönde kaydırma yapar.
#
# 2. satır [0, 1, 90]
#    - 0: x eksenine etkisi, 0 olduğu için y koordinatları x'yi etkilemez.
#    - 1: y eksenine etkisi, 1 olduğu için y ekseni boyunca kaydırma yapılmaz, orijinal y değerleri korunur.
#    - 90: y ekseninde 90 birimlik pozitif yönde kaydırma yapar.
M = np.float32([[1, 0, 300],  # x ekseni kaydırması
                [0, 1, 90]])  # y ekseni kaydırması

# Küçük resmi belirtilen matris M'ye göre kaydırır ve yeni bir görüntü oluşturur
shifted = cv.warpAffine(res, M, (cols, rows))

cv.imshow("small", res)  # Küçük resmi gösterir
cv.waitKey(0)  # Klavyeden bir tuşa basılana kadar bekler

# Yeniden küçük resmin kaydırılmasını gerçekleştirir
shifted = cv.warpAffine(res, M, (cols, rows))
cv.imshow("shifted", shifted)  # Kaydırılmış küçük resmi gösterir
cv.waitKey(0)  # Klavyeden bir tuşa basılana kadar bekler

# Dönüşüm matrisini oluşturur
# (cols/2, rows/2) resmin merkezi etrafında dönüş yapılmasını sağlar
# 90, döndürme açısı (derece cinsinden)
# 1, ölçek faktörüdür, yani boyutu değiştirmez
M = cv.getRotationMatrix2D((cols/2,rows/2,),90,1)

# Resmi belirtilen matris M'ye göre döndürür ve yeni bir görüntü oluşturur
dst =cv.warpAffine(res,M,(cols,rows))

cv.imshow("img",dst) # Döndürülmüş resmi gösterir
cv.waitKey(0)
cv.destroyAllWindows()  # Tüm açık pencereleri kapatır
