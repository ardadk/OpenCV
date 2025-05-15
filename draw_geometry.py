import cv2 as cv
import numpy as np

image = np.zeros((512,512,3),dtype=np.uint8)
#512x512 boyutunda 0'lardan oluşan array oluşturduk.
#0'lardan oluştuğu için siyah bir image'dir

cv.rectangle(image,(100,100),(300,300),(255,0,0),2,cv.LINE_8,0)
#ilk parametre işleneceği image'i tutar.
#2.parametre sol üst köşe koordinatı
#3.parametre sağ alt köşe koordinatı
#4.parametre dikdörtgenin rengini temsil eder.
#5.parametre çizgi kalınlığını temsil eder.-1 girilirse dikdörtgen içi boyalı çizilir.
#6.parametre (cv.LINE_8) çizgi fontunu temsil eder.
#7.parametre çizginin koordinatlarını etkileyen bir kaydırma değeri. Varsayılan olarak 0 girilir (kaydırma yoktur).
cv.circle(image,(256,256),50,(0,0,255),2,cv.LINE_8,0)
#ilk parametre işleneceği image'i tutar.
#2. parametre çemberin merkezi koordinatlarını temsil eder.
#3.parametre çizilen çemberin yarıçapını temsil eder
#4.parametre çemberin rengini temsil eder.
#5.parametre çizgi kalınlığını temsil eder. Yine -1 girilirse içi dolu çizilir.
#6.parametre çizgi fontunu temsil eder.
#7.parametre çizginin koordinatlarını etkileyen bir kaydırma değeri. Varsayılan olarak 0 girilir (kaydırma yoktur).
cv.ellipse(image,(256,256),(150,50),360,0,360,(0,255,0),2,cv.LINE_8,0)
#ilk parametre işleneceği image'i tutar.
#2.parametre elipsin merkezi koordinatlarını temsil eder.
#3.parametre elipsin eksen uzunluklarıdır. 150 büyük eksen yarıçapı 50 küçük eksen yarıçapı
#4.parametre elipsin dönme açısını temsil eder.
#5.parametre elipsin başlangıç ve bitiş açılarını temsil eder.
#6.parametre elipsin rengini temsil eder.
#7.parametre çizgi kalınlığını temsil eder.Yine -1 girilirse içi dolu çizilir.
#8.parametre çizgi fontudur.
#9.parametre çizginin koordinatlarını etkileyen bir kaydırma değeri. Varsayılan olarak 0 girilir (kaydırma yoktur).
cv.imshow("image",image)
cv.waitKey(0)

for i in range(100000):
    image[:,:,:]=0
    x1 = np.random.rand()*512
    y1 = np.random.rand()*512
    x2 = np.random.rand()*512
    y2 = np.random.rand()*512

    b=np.random.randint(0,256)
    g = np.random.randint(0, 256)
    r = np.random.randint(0, 256)
    cv.line(image,(int(x1),int(y1)),(int(x2),int(y2)),(b,g,r),4,cv.LINE_8,0)
    cv.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (b, g, r), 1, cv.LINE_8, 0)
    cv.imshow("image",image)
    c=cv.waitKey(20)
    if c == 27:
        break
cv.destroyAllWindows()
