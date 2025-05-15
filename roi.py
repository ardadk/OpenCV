import cv2 as cv

#ROI ( Region of interest )

src = cv.imread("qfai.jpg")

h,w = src.shape[:2] #image'in boyutlarını gördük
print(h,w)
img =  src.copy() # kopyasını aldık

roi = img[250:750,200:800,:] #odaklanılacak alanı seçtik
cv.imshow("roi",roi)
cv.waitKey(0)

img[0:500,0:600,:]=roi   # orjinal image'deki seçili bir alana odaklandığımız bölgeyi yapıştırdık.
cv.imshow("img",img)
cv.waitKey(0)

res = cv.resize(roi,None,fx=0.3,fy=0.3,interpolation=cv.INTER_CUBIC) #daha küçük bir odak image'i elde ettik
cv.imshow("res",res)
cv.waitKey(0)

print(res.shape) #küçültülmüş odak bölgesinin boyutlarını alıp büyük image'e yapıştıracaz

src[0:150,0:180,:] = res # küçültülmüş roi'yi yapıştırdık ve gösterdik
cv.imshow("src",src)
cv.waitKey(0)
