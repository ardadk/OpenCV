import numpy as np
import cv2 as cv

path = "C:/Users/Arda/Desktop/OpenCV/"
img = cv.imread(path+"qfai.jpg")
cv.namedWindow("image create", cv.WINDOW_AUTOSIZE)
cv.imshow("image create", img)
cv.waitKey(0)

m1 = np.copy(img)  #m1 değişkenine img array'ını kopyaladık.
m2 = img #img değişkenini m2'ye eşitledik

img[100:200,200:300,:] =255 #array'ın seçili alanlarını hexadecimaldeki 255 rakamına yani beyaz renge çevir.
cv. imshow("m2",m2)
cv.waitKey(0)

m3 = np.zeros(img.shape,img.dtype)  #img array'ının matrislerini 0'la yani siyah renge dönüştür
cv.imshow("m3",m3)
cv.waitKey(0)

m4 = np.zeros([512,512],np.uint8) #[512,512] parametresi oluşturalacak dizinin boyutunu belirler
                                         #np.uint8 parametesi "unsigned integer 8-bit" dizinin elemanlarının veri tipini gösterir
                                         # yani her eleman 0 ile 255 arasında bir değer alabilir.
cv.imshow("m4",m4)
cv.waitKey(0)

m5 = np.zeros([512,512],np.uint8)  #m5 adında 512x512 boyutunda 0'lardan oluşan bir dizi oluştur.Yani siyah renkte
cv.imshow("m5",m5)
cv.waitKey(0)
m6 = np.copy(m5)
m6[:,:] = 127 # 0'lardan oluşan bu dizinin tüm satır ve sütunlarını 127'ye çevir. Yani gri renge döndür
cv.imshow("m6",m6)
cv.waitKey(0)


dortgen = np.ones((550,770,3))
# 550x770x3 boyutlarında tüm elemanları "1" olan bir array oluşturduk.


black = (0,0,0) # siyah renginin array karşılığı
red = (0,0,255) #kırmızı renginin array karşılığı
green = (0,255,0) # yeşil renginin array karşılığı



#CV.RECTANGLE METHODU


cv.rectangle(dortgen,(480,250),(100,450),black,8)
# cv.rectangle diktörtgen oluşturmak için bir methoddur.
#ilk parametre dortgen şeklin çizileceği image değişkenidir.
#(480,250) yani 2.parametre dikdörtgenin sol üst köşesinin koordinatıdır.
#(100,450) yani 3.parametre dikdörtgenin sağ alt köşesinin koordinatıdır.
#black yani 4. parametre çizilen dikdörtgenin rengini temsil eder. black değişkenine (0,0,0) atadığımız için siyah renkte oluşur.
#son parametre yani "8" çizgilerin kalınlığını temsil eder. Yani dikdörtgenin kenarları 8 piksel kalınlığında olacaktır.
cv.rectangle(dortgen,(580,150),(200,350),black,8)
#dikdörtgen prizma oluşturacağımız için bir adet daha dikdörtgen oluşturduk


#CV.LINE METHODU


cv.line(dortgen,(100,450),(200,350),black,8)
#cv.line çizgi çizmek için bir methoddur.
#ilk parametre yani dortgen çizginin çizileceği image değişkenidir.
#2. parametre yani (100,450) çizginin başlangıç noktasının koordinatıdır.
#3. parametre yani (200,350) çizginin bitiş noktasının koordinatıdır.
#4. parametre yani black çizginin rengini temsil eder. black değişkeni (0,0,0) olduğu için rengimiz siyah olacaktır.
#son parametre yani "8" çizgi kalınlığını temsil edecektir.
cv.line(dortgen,(480,250),(580,150),black,8)
cv.line(dortgen,(100,250),(200,150),black,8)
cv.line(dortgen,(480,450),(580,350),black,8)
#oluşturduğum 2 dikdörtgenin aralarını çizerek bir prizma elde ettik.

#cv.putText METHODU

start_point = (150,100) # Metnin yazılmaya başlanacağı noktanın koordinat bilgileri
font_thickness = 2 # Metin fontunun kalınlığı
font_size = 5 # Metin fontunun boyutu
font  = cv.FONT_HERSHEY_DUPLEX # Font türü

cv.putText(dortgen,"ardadk",start_point,font,font_size,green,font_thickness)
#İlk parametre image değişkenini temsil eder
#2.parametre yazılacak metin stringini temsil eder
#3.parametre yani start_point metnin yazılmaya başlanacağı noktayı temsil eder.
#4.parametre font türünü temsil eder.
#5.parametre font boyutunu temsil eder.
#6.parametre metnin rengini temsil eder.
#Son parametre ise font kalınlığını temsil eder.
cv.imshow("dortgen",dortgen)
cv.waitKey(0)