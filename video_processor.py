import cv2
import time
from detection.yolo_detector import detect_people
from analytics.analytics_store import update_zone_count
from analytics.analytics_store import store_history
from alerts.alert_store import check_alert

caps = {}

CAMERA_ZONE_MAP = {
    1: "zone1",
    2: "zone2",
    3: "zone3",
    4: "zone4",
}

def init_videos(video_sources):
    for cam_id, path in video_sources.items():
        caps[cam_id] = cv2.VideoCapture(path)
    print("✅ Videos initialized")

def process_frames():
    print("🔥 Video processing started")

    while True:
        for cam_id, cap in caps.items():
            ret, frame = cap.read()

            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            people_count = detect_people(frame)
            zone = CAMERA_ZONE_MAP[cam_id]

            print(f"[YOLO] {zone}: {people_count}")
            
            # ✅ Update analytics
            update_zone_count(zone, people_count)
            
            # ✅ Store historical data (FIXED LOCATION)
            store_history(cam_id, zone, people_count)

            if check_alert(zone, people_count):
               print(f"🚨 ALERT: {zone} exceeded threshold")

        time.sleep(2.5)  # update every second

