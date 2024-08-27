import cv2

# cap = cv2.VideoCapture('/dev/bus/usb/001/002')  # Change to 1 if using an external webcam
cap = cv2.VideoCapture('/dev/video0')
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
# https://stackoverflow.com/questions/72255353/wsl-webcam-usb-can-not-open-camera-by-index
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()