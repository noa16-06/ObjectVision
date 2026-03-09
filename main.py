from ultralytics import YOLO
import cv2

def yolo_object_detector():
    model = YOLO("yolov8n.pt")  # n = nano (fast)

    cap = cv2.VideoCapture(0)

    colors = {
        "person": (0, 255, 0),
        "cell phone": (255, 0, 0),
        "laptop": (0, 0, 255)
    }

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        results = model(frame, stream=True)

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                label = model.names[cls]

                # Draw a Recktangel
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2

                color = colors.get(label, (0, 255, 255))
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.circle(frame, (cx, cy), 5, (0, 0, 0), -1)
                cv2.putText(frame, f"{label} {conf:.2f}",
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, color, 2)

        cv2.imshow("YOLO Object Detector", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

yolo_object_detector()
