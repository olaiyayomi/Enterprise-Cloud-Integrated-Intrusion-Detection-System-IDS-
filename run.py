import cv2
import requests
import time
import os
from ultralytics import YOLO
TELEGRAM_TOKEN = "8949258032:AAEkO-LU_lWt3WXHTByJtfZ8tkMHJ9cleq0"
TELEGRAM_CHAT_ID = "6697757264"

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("C:/Users/USER/Downloads/intruder_vid.webm")

cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

last_alert_time = 0
ALERT_COOLDOWN = 15 

print("Zero Lag, Cloud Integrated Security System is Live...")

def send_telegram_photo(image_path, caption):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "caption": caption, "parse_mode": "Markdown"}
    try:
        with open(image_path, 'rb') as photo_file:
            files = {"photo": photo_file}
            response = requests.post(url, data=payload, files=files)
        if response.status_code == 200:
            print("Successfully sent to cloud endpoint.")
        else:
            print(f"Telegram Error: {response.text}")
    except Exception as e:
        print(f"Failed to transmit: {e}")

while cap.isOpened():
    #cap.grab() 
    success, frame = cap.read()
    if not success:
        break

    results = model(frame, classes=[0], conf=0.60, max_det=2, imgsz=320)
    person_detected = False

    if len(results[0].boxes) > 0:
        person_detected = True

    annotated_frame = results[0].plot()

    if person_detected and (time.time() - last_alert_time > ALERT_COOLDOWN):
        print("INTRUSION DETECTED! Processing fresh snapshot...")
        
        temp_filename = "intruder_alert.jpg"
        cv2.imwrite(temp_filename, annotated_frame)
        
        alert_msg = "*SECURITY ALERT:* Target isolated. Zero-latency stream capture attached."
        send_telegram_photo(temp_filename, alert_msg)
        
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
            
        last_alert_time = time.time()

    cv2.imshow("Enterprise IDS - Edge AI Feed", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()