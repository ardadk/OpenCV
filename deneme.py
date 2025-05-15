import cv2

# Giriş ve çıkış video dosyası adları
input_path = 'sora.mp4'  # Kullanıcının yüklediği video dosyasının yolu
output_path = 'output3_video.mp4'  # Yeniden boyutlandırılmış videonun çıktı yolu

# Video dosyasını oku
cap = cv2.VideoCapture(input_path)

# Orijinal video çerçeve hızı, codec ve çıkış dosyası için VideoWriter nesnesi oluştur
fps = cap.get(cv2.CAP_PROP_FPS)  # Orijinal videonun fps değeri
if fps == 0:  # FPS değeri 0 ise, varsayılan bir değer kullanılır
    fps = 30.0
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec (MP4 için genellikle 'mp4v' kullanılır)

# Video yazıcısını 550x1080 boyutunda oluştur
out = cv2.VideoWriter(output_path, fourcc, fps, (1920, 550))

while True:
    # Her kareyi oku
    ret, frame = cap.read()

    # Videonun sonuna gelindiyse, işlemi durdur
    if not ret:
        break

    # Kareyi 550x1080 boyutuna yeniden boyutlandır
    resized_frame = cv2.resize(frame, (1920, 550))

    # Yeniden boyutlandırılan kareyi çıkış videosuna yaz
    out.write(resized_frame)

# Kaynakları serbest bırak
cap.release()
out.release()
cv2.destroyAllWindows()
