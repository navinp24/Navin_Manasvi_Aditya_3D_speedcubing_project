import cv2
import numpy as np
import time

def get_average_color(frame, bbox):
    x, y, w, h = bbox
    roi = frame[y:y+h, x:x+w]
    avg_color = cv2.mean(roi)[:3]  # B, G, R
    return tuple(map(int, avg_color))

cap = cv2.VideoCapture(0)
saved_colors = []
MAX_COLORS = 54
COOLDOWN = 5.0  # seconds between auto-captures

last_capture_time = 0.0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    display = frame.copy()

    # Pre-process
    blurred = cv2.GaussianBlur(frame, (5,5), 0)
    gray    = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    edges   = cv2.Canny(gray, 50, 150)

    # Find & filter contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    squares = []
    for cnt in contours:
        peri   = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
        if len(approx) == 4 and cv2.isContourConvex(approx):
            area = cv2.contourArea(approx)
            if area < 1000:
                continue
            x,y,w,h = cv2.boundingRect(approx)
            ar = w/float(h)
            if 0.8 < ar < 1.25:
                squares.append((approx,(x,y,w,h)))

    # Choose border color (red until exactly 9)
    border_color = (0,255,0) if len(squares)==9 else (0,0,255)
    for approx,_ in squares:
        cv2.drawContours(display, [approx], -1, border_color, 2)

    # Overlay status text
    elapsed = time.time() - last_capture_time
    if len(squares)==9 and elapsed < COOLDOWN:
        status = f"Captured! Next in {int(COOLDOWN-elapsed)}s"
    elif len(squares)==9:
        status = "Ready to capture"
    else:
        status = f"Looking for 9 squares ({len(squares)}/9)"
    cv2.putText(display, status, (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

    cv2.putText(display,
                f"Saved: {len(saved_colors)}/{MAX_COLORS}",
                (10,60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

    cv2.imshow("Auto Rubik Face Scanner", display)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or len(saved_colors) >= MAX_COLORS:
        break

    # Auto-capture logic
    now = time.time()
    if len(squares)==9 and (now - last_capture_time) >= COOLDOWN:
        # capture these 9
        for _, bbox in squares:
            saved_colors.append(get_average_color(frame, bbox))
        face_number = len(saved_colors)//9
        print(f"\nCaptured Face {face_number}:")
        for col in saved_colors[-9:]:
            print(col)
        last_capture_time = now

cap.release()
cv2.destroyAllWindows()

print("\nFinal Saved Colors:")
for i, col in enumerate(saved_colors, 1):
    print(f"{i:2d}: {col}")
