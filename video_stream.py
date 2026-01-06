import cv2
import time
from detection.yolo_detector import detect_people


cv2.setNumThreads(1)

VIDEO_PATHS = {
    1: "videos/cam1.mp4",
    2: "videos/cam2.mp4",
    3: "videos/cam3.mp4",
    4: "videos/cam4.mp4",
}

caps = {}

def get_cap(cam_id):
    if cam_id not in caps:
        cap = cv2.VideoCapture(VIDEO_PATHS[cam_id])
        caps[cam_id] = cap
    return caps[cam_id]

def generate_frames(cam_id):
    cap = get_cap(cam_id)

    while True:
        ret, frame = cap.read()

        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 🔁 loop video
            continue

        count = detect_people(frame)

        _, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()

        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" +
               frame + b"\r\n")

        time.sleep(0.03)
