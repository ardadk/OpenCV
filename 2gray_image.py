import cv2 as cv #kütüphane importu


###Basit Image Okuma
path = "C:/Users/Arda/Desktop/OpenCV/" #path yolunu kaydettik
img = cv.imread(path+"qfai.jpg") #img değişkeine imread'le yolu kaydettik

###cvtColor ile Renk Değişimi
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  #ilk parametre image'i ikinci parametre ise dönüştürmek istediğimiz rengi temsil eder
cv.imshow("gray", gray) #resmi göster
cv.waitKey(0)

###imwrite ile kaydetme
cv.imwrite(path+"gray_qfai.jpg", gray)  #ilk parametreye kaydetmek istediğimiz ismi girdik ikinciye ise kaydedeceğimiz image'i
cv.destroyAllWindows()

img = cv.imread(path+"qfai.jpg", cv.IMREAD_GRAYSCALE) # direkt olarak resmi gri renkle okuma işlemi
cv.namedWindow("gray", cv.WINDOW_AUTOSIZE)
cv.imshow("gray", img)
cv.waitKey(0)
