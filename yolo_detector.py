from ultralytics import YOLO
import cv2

# Load YOLOv8 model once (IMPORTANT for performance)
model = YOLO("yolov8n.pt")

def detect_people(frame):
    """
    Detects people in a frame using YOLOv8
    Returns: number of people detected
    """

    results = model(frame, stream=False, conf=0.4)

    count = 0

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])

            # COCO class 0 = person
            if cls_id == 0:
                count += 1

                # OPTIONAL: draw bounding box (for video preview)
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    "Person",
                    (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )

    return count
