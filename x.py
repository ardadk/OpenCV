import cv2
import numpy as np
from ultralytics import YOLO
from playsound import playsound  # Ses çalmak için kütüphane

# 1️⃣ YOLO modelini yükle
model = YOLO("yolov8n.pt")  # YOLOv8 Nano modeli

# 2️⃣ Video yakalama
cap = cv2.VideoCapture("videoplayback.mp4")  # Kendi kameran için


def is_within_risk_zone(center_x, center_y, start_point, left_point, right_point):
    """Risk alanının içinde olup olmadığını kontrol et"""
    if center_x > left_point[0] and center_x < right_point[0]:
        return True
    return False


def is_growing(area, previous_area, growth_threshold=5000, abnormal_growth_threshold=15000):
    """Alan büyümesini kontrol et"""
    if previous_area is None:
        return False, False
    growth_rate = area - previous_area
    abnormal_growth = growth_rate > abnormal_growth_threshold
    return growth_rate > growth_threshold, abnormal_growth


previous_areas = {}  # Her araç için önceki alanı tutan bir sözlük
alarm_playing = False  # Alarmın tekrar tekrar çalmasını önlemek için

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 3️⃣ YOLO ile araç tespiti yap
    results = model(frame)

    # 4️⃣ Risk alanını çiz (örneğin, 30° ve -30° açı ile)
    height, width = frame.shape[:2]
    start_point = (width // 2, height)
    left_point = (int(width * 0.2), 0)
    right_point = (int(width * 0.8), 0)
    cv2.line(frame, start_point, left_point, (0, 255, 0), 2)
    cv2.line(frame, start_point, right_point, (0, 255, 0), 2)

    # 5️⃣ Araçların tespiti
    for box in results[0].boxes:  # Sonuçlardaki her bir kutu
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()  # Sınırlayıcı kutunun dört köşesini al
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        # Risk alanı içinde mi kontrol et
        if is_within_risk_zone(center_x, center_y, start_point, left_point, right_point):
            area = (x2 - x1) * (y2 - y1)  # Kutunun alanını hesapla
            box_id = hash(f"{x1}{y1}{x2}{y2}")  # Araca özel bir kimlik atamak için hash kullan
            previous_area = previous_areas.get(box_id)

            growing, abnormal_growth = is_growing(area, previous_area)  # Büyüme oranını kontrol et

            if growing:  # Eğer alan büyüyorsa
                cv2.putText(frame, "UYARI!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            if abnormal_growth and not alarm_playing:  # Eğer anormal büyüme varsa alarmı çal
                alarm_playing = True
                playsound('alarm.wav', block=False)  # Ses çal
                print("🚨 Anormal Büyüme Algılandı - Alarm Çalıyor! 🚨")

            previous_areas[box_id] = area  # Güncel alanı kaydet

        # Kutuyu çiz
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
        cv2.circle(frame, (int(center_x), int(center_y)), 5, (255, 0, 0), -1)  # Orta noktayı çiz

    # Çerçeveyi göster
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
