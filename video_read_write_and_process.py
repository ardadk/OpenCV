import cv2 as cv

capture = cv.VideoCapture(0)
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT) #kamera videosunun yüksekliği
width = capture.get(cv.CAP_PROP_FRAME_WIDTH) #kamera videosunun genişliği
count = capture.get(cv.CAP_PROP_FRAME_COUNT) #kamera videosundaki toplam kare(frame) sayısını temsil eder.
fps = capture.get(cv.CAP_PROP_FPS) #kamera videosunun fps'ini temsil eder.
print(height,width,count,fps)

def process(image,opt=1):
    dst=None
    if opt==0:
        dst = cv.bitwise_not(image) # renkleri tersine dönüştürme
    if opt==1:
        dst=cv.GaussianBlur(image,(0,0),15) #blurlama işlemi
    if opt==2:
        dst=cv.Canny(image,100,200) #kenarları belirleme
    return dst
index = 2
while True:
    ret,frame =capture.read()
    if ret is True:
        cv.imshow("video-input",frame)
        c = cv.waitKey(50)
        if c >=49:
            index = c-49
        result=process(frame,index)
        cv.imshow("result",result)
        if c == 27:
            break
    else:
        break

cv.waitKey(0)
