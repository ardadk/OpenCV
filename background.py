import cv2 as cv

# Video dosyasını yükle
cap = cv.VideoCapture("a.mp4")

# Arka plan çıkarıcı oluştur
fgbg = cv.createBackgroundSubtractorMOG2(history=250, varThreshold=100)

while True:
    ret, frame = cap.read()

    # Eğer video biterse döngüyü kır
    if not ret:
        break

    # Arka planı çıkar ve maskeyi oluştur
    fgmask = fgbg.apply(frame)
    background = fgbg.getBackgroundImage()

    # Çerçeveleri göster
    cv.imshow("Input", frame)
    cv.imshow("Mask", fgmask)

    if background is not None:
        cv.imshow("Background", background)

    # Her kare için 30 ms bekle, ESC'ye basıldığında çık
    k = cv.waitKey(30) & 0xff
    if k == 27:  # ESC tuşu
        break

# Tüm pencereleri kapat ve bellekten temizle
cap.release()
cv.destroyAllWindows()
