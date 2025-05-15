
import cv2 as cv
import numpy as np

capture = cv.VideoCapture("video.mp4")
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT) #videonun yüksekliği
width = capture.get(cv.CAP_PROP_FRAME_WIDTH) #videonun genişliği
count = capture.get(cv.CAP_PROP_FRAME_COUNT) #videodaki toplam kare(frame) sayısını temsil eder.
fps = capture.get(cv.CAP_PROP_FPS) #videonun fps'ini temsil eder.
print(height,width,count,fps)

out = cv.VideoWriter("video.avi",cv.VideoWriter_fourcc("D","I","V","X"),15,
                     (int(width),int(height)),True)
#video kaydetmek için kullanılır.
#ilk parametre kaydedilecek videnonun ismini ifade eder.
#cv.VideoWriter_fourcc("D","I","V","X") video codec'ini temsil eder.
#15 fps değeridir
#(int(width),int(height)) kaydedilecek videonun çözünürlüğünü temsil eder.
#True ise çıktı olacak videonun renkli olup olmadığını temsil eder.True renkli False siyah-beyaz

while True:
    ret,frame = capture.read() #ret görüntünün varlığını temsil eden bir değişken
                               #frame ise videodaki her bir kareyi temsil eder.
    if ret is True: #görüntü varsa
        cv.imshow("video",frame)#videoyu göster
        out.write(frame)#her bir kareyi videoya yaz
        a=cv.waitKey(50)#50 saniye sonra kapat
        if a==27: #ESC tuşuna basarsa videoyu kapat
            break
    else:
        break

capture.release()#serbest bırak
out.release()#serbest bırak

