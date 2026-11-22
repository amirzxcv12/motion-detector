import cv2

# The webcam provides the live video feed.
camera = cv2.VideoCapture(0)

# Background subtraction helps separate moving objects from the scene.
background = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=35,
    detectShadows=True
)

if not camera.isOpened():
    raise SystemExit("Could not open the webcam.")

while True:
    success, frame = camera.read()
    if not success:
        print("Could not read a frame.")
        break

    frame = cv2.flip(frame, 1)

    # Create a mask that highlights changes from the background.
    mask = background.apply(frame)

    # Remove some small noise before finding moving areas.
    _, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
    mask = cv2.medianBlur(mask, 5)

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        # Ignore tiny changes such as sensor noise.
        if cv2.contourArea(contour) < 1200:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frame, "Motion detected", (x, max(25, y - 10)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2
        )

    cv2.imshow("Motion Detector", frame)
    cv2.imshow("Motion Mask", mask)

    # Press Q to close both windows.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
