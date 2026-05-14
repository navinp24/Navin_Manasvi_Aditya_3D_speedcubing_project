from cv2 import (VideoCapture, imshow, waitKey, destroyAllWindows,GaussianBlur, Canny, cvtColor, COLOR_BGR2GRAY,findContours, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE,arcLength, approxPolyDP, contourArea, isContourConvex,boundingRect, drawContours, putText, FONT_HERSHEY_SIMPLEX)
from numpy import *

def is_square(cnt, epsilon_coef=0.02, min_area=1000):
    """Return (True, bbox, approx) if cnt is a roughly square contour."""
    peri   = arcLength(cnt, True)
    approx = approxPolyDP(cnt, epsilon_coef * peri, True)
    if len(approx) == 4 and isContourConvex(approx):
        area = contourArea(approx)
        if area > min_area:
            x, y, w, h = boundingRect(approx)
            ar = w / float(h)
            if 0.8 <= ar <= 1.2:
                return True, (x, y, w, h), approx
    return False, None, None

def main():
    cap = VideoCapture(1)  
    if not cap.isOpened():
        print("Cannot open camera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray  = cvtColor(frame, COLOR_BGR2GRAY)
        blur  = GaussianBlur(gray, (5, 5), 0)
        edges = Canny(blur, 50, 150)

        contours, _ = findContours(edges, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)
        squares = []
        for cnt in contours:
            ok, bbox, approx = is_square(cnt)
            if ok:
                squares.append((bbox, approx))
# label when 9 sq detect 
        if len(squares) == 9:

            cells = []
            for bbox, approx in squares:
                x, y, w, h = bbox
                cx = x + w / 2
                cy = y + h / 2
                cells.append({
                    'bbox':   bbox,
                    'approx': approx,
                    'cx':     cx,
                    'cy':     cy
                })
            # Sort all cells left→right by center-x, then split into 3 columns
            cells.sort(key=lambda c: c['cx'])
            cols = [cells[i*3:(i+1)*3] for i in range(3)]

            # Within each column, sort top→bottom by center-y
            for col in cols:
                col.sort(key=lambda c: c['cy'])

            # Draw & label in column-major order
            for col_idx, col in enumerate(cols):
                for row_idx, cell in enumerate(col):
                    idx = col_idx * 3 + row_idx  # 0..8
                    x, y, w, h = cell['bbox']
                    drawContours(frame, [cell['approx']], -1, (0,255,0), 2)
                    putText(
                        frame,
                        str(idx),
                        (int(x), int(y) - 10),
                        FONT_HERSHEY_SIMPLEX,
                        0.9,
                        (255,255,255),
                        2
                    )
            putText(frame, "Layout: 0 3 6 / 1 4 7 / 2 5 8",
                    (10, frame.shape[0] - 20),
                    FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)
        
            # If not 9, just draw whatever squares found and show count
        for bbox, approx in squares:
                drawContours(frame, [approx], -1, (0,0,255), 2)
        putText(
                frame,
                f"Detected {len(squares)} squares",
                (10, 30),
                FONT_HERSHEY_SIMPLEX,
                1.0,
                (0,0,255),
                2
            )

        # Show result
        imshow('Cube Face Indexing', frame)

        # Exit on ESC
        if waitKey(1) & 0xFF == 27:
            break

    cap.release()
    destroyAllWindows()

if __name__ == "__main__":
    main()
