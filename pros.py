from cv2 import VideoCapture,imshow,waitKey,destroyAllWindows

cap = VideoCapture(0) # this means it will open the first camera of the computer 

if not cap.isOpened():
    print("Cannot open camera")
    exit()
#   the use of ths while loop is to keep the camera open until the user presses the 'q' key
while True :
    ret, frame = cap.read()
    if not ret: 
        print("Can't receive frame (stream end?). Exiting ...")
        break 

    imshow('Camera', frame)
    if waitKey(1) == ord('q'): #if q preessed then the window will closeq 0, delay = zero means infinite delay for key presses
        destroyAllWindows()
        exit()