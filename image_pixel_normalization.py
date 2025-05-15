import numpy as np
import cv2 as cv
img = cv.imread("qfai.jpg")

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) #image'i gri tonlamaya çevirdik.
cv.imshow("gray",gray)
cv.waitKey(0)

#NORM_MINMAX Normalizasyonu
gray = np.float32(gray) # normalizsayon işlemlerinde yuvarlama olmasın diye integer tipindeki array'leri float cinsine çevirdik.
print(gray)

dst = np.zeros(gray.shape,dtype=np.float32) #0'lardan oluşan gray image'inin boyutlarında float türünde bir array oluştur.

cv.normalize(gray,dst=dst,alpha=0,beta=1.0,norm_type=cv.NORM_MINMAX)
#İlk parametresi normalize işlemi uygulanacak image'i temsil eder.
#dst parametresi normalize edildikten sonra normalize edilmiş array'ın hangi array'ın üstüne kaydedileceğini yani çıkış array'ını temsil eder.
#alpha parametresi normalize işlemindeki min değeri temsil eder.
#beta parametresi normalize işlemindeki max değeri temsil eder.
#norm_type parametresi hangi normalize işlemini uygulayacağımızı temsil eder.
#bütün renk değerleri 0 ile 1 arasında kendi değerlerine karşılık bir yere sıkıştırıldı.
#Makine Öğrenmesindeki StandartScaler gibidir.

print(dst)
dst = np.uint8(dst*255) #float türündeki array'ı normalize ettiğimizde değerleri 0 ile 1 arasında yer aldı ve
                        #tekrardan integer tipine dönmek istersek bu sefer direkt np.astype(int) dersek float
                        #değerler yuvarlanacağı için görüntü sadece siyah ve beyazlardan oluşucak bunun yerine
                        #255 ile çarpmamız yeterli olacaktır.
print(dst)

#NORM_INF Normalizasyonu
dst = np.zeros(gray.shape,dtype=np.float32)
cv.normalize(gray,dst=dst,alpha=0,beta=1.0,norm_type=cv.NORM_INF)
cv.imshow("NORM_INF",np.units(dst*255))
cv.waitKey(0)

#NORM_L1 Normalizasyonu
dst = np.zeros(gray.shape,dtype=np.float32)
cv.normalize(gray,dst=dst,alpha=0,beta=1.0,norm_type=cv.NORM_L1)
cv.imshow("NORM_L1",np.units(dst*10000000))
cv.waitKey(0)

#NORM_L2 Normalizasyonu
dst = np.zeros(gray.shape,dtype=np.float32)
cv.normalize(gray,dst=dst,alpha=0,beta=1.0,norm_type=cv.NORM_L2)
cv.imshow("NORM_L2",np.units(dst*10000))
cv.waitKey(0)