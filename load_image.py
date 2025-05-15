import cv2 as cv #kütüphane importu


###Basit Image Okuma
path = "C:/Users/Arda/Desktop/OpenCV/" #path yolunu kaydettik
img = cv.imread(path+"qfai.jpg") #img değişkeine imread'le yolu kaydettik

cv.namedWindow("image", cv.WINDOW_AUTOSIZE) # açılır pencerenin ismi ve boyutunu girdik boyut parametresi otomatik olarak girildi

cv.imshow("image", img) # resmi göster
cv.waitKey(0) #konsolu meşgul etmesi için girildi
cv.destroyAllWindows() # bütün pencereleri kapat
