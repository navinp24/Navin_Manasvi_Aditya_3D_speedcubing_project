from cv2 import VideoCapture, imshow, waitKey, destroyAllWindows, GaussianBlur, cvtColor, COLOR_BGR2GRAY,Canny

cap = VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Convert to grayscale
    gray = cvtColor(frame, COLOR_BGR2GRAY)
    egdes = Canny(frame , 30, 150)

    # Optionally apply blur to grayscale image
    blurred = GaussianBlur(gray, (11, 11), 0) # to remnove the noise from the image and make it smoother, goof for edge detection 

    # Show the blurred grayscale image
    imshow('Camera (Grayscale + Blur)', gray) # to show which part to be shown 

    if waitKey(1) == ord('q'):
        break

destroyAllWindows()
cap.release()
