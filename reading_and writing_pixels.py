import numpy as np
import cv2 as cv

path = "C:/Users/Arda/Desktop/OpenCV/"
img = cv.imread(path+"qfai.jpg")
cv.namedWindow("img", cv.WINDOW_AUTOSIZE)

h,w,ch = img.shape  #matrisin boyutlarını h ,w , ch adlı değişkenlere atadık
                    #h = height , w= width , ch = channel
                    #height = Görüntünün dikey eksende kaç piksel yüksekliğe sahip olduğunu ifade eder.
                    #width = Görüntünün yatay eksende kaç piksel genişliğe sahip olduğunu ifade eder.
                    #channel = Görüntünün kaç renk kanalına sahip olduğunu belirtir.
                    #channel 1 olduğunda: Gri tonlu görüntü (tek renk).
                    #channel 3 olduğunda: RGB renkli görüntü (kırmızı, yeşil, mavi kanalları).
                    #channel 4 olduğunda: RGBA (RGB'ye ek olarak alpha kanalı, yani şeffaflık).


for row in range(h):  # height matrisinde yani görüntünün satırlarında row değişkenini gezdir
    for col in range(w): # row değişkeni gezerken width matrisinde yani görüntünün sütunlarında col değişkenini gezdir
        b,g,r = img[row,col] # b, g, r değişkenlerine her koordinattaki renk bileşenlerini atadık.
        b= 255-b # b değişkenini 255'den çıkartıp beyazları siyah yaptık
        g = 255-g #g değişkenini 255'den çıkartıp beyazları siyah yaptık
        r = 255-r #r değişkenini 255'den çıkartıp beyazları siyah yaptık
        img[row,col] = (b,g,r) # elde ettiğimiz değerleri görüntüde güncelledik.

#!!!Döngüde RGB(r,g,b) şeklinde değil de BGR(b,g,r) şeklinde sıraladık bunun sebebi openCV'nin renkleri BGR formatında saklamasıdır!!!

cv.imshow("img", img)
cv.waitKey(0)

cv.destroyAllWindows()
cv.imread(path+"qfai.jpg")