import cv2
import winsound

# Constants
FRAME_THRESHOLD = 20   # Number of consecutive frames to trigger alarm

# Load Haar Cascade Classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

cap = cv2.VideoCapture(0)
closed_frames = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Couldn't read frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Detect eyes inside the face region
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        if len(eyes) == 0:  # No eyes detected → Possible drowsiness
            closed_frames += 1
            if closed_frames >= FRAME_THRESHOLD:
                cv2.putText(frame, "DROWSINESS ALERT!", (100, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                print("🔔 ALARM: Driver is Drowsy!")
                winsound.Beep(2000, 1000)  # Beep sound (frequency, duration)
        else:
            closed_frames = 0  # Reset counter if eyes are detected

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
