import cv2
from numpy import *
from time import *

COOLDOWN = 5.0

def get_basic_color(avg_color):
    pixel = uint8([[avg_color]])
    h, s, v = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)[0][0]
    if v > 200 and s < 30:
        return 'white'
    if   h < 10 or h >= 170: return 'R'
    elif 10 <= h < 25:       return 'O'
    elif 25 <= h < 35:       return 'Y'
    elif 35 <= h < 85:       return 'G'
    elif 85 <= h < 125:      return 'B'
    else:                    return 'R'  # fallback

def get_avg_color(frame, bbox):
    x, y, w, h = bbox
    roi = frame[y:y+h, x:x+w]
    b, g, r, _ = cv2.mean(roi)
    return (int(b), int(g), int(r))

def is_square(cnt, eps_coef=0.02, min_area=1000):
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, eps_coef * peri, True)
    if len(approx) == 4 and cv2.isContourConvex(approx):
        area = cv2.contourArea(approx)
        if area > min_area:
            x, y, w, h = cv2.boundingRect(approx)
            ar = w / float(h)
            if 0.8 <= ar <= 1.2:
                return True, (x, y, w, h), approx
    return False, None, None

def main():
    last_capture = 0.0
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        edges = cv2.Canny(blur, 50, 150)

        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        squares = []
        for cnt in contours:
            ok, bbox, approx = is_square(cnt)
            if ok:
                squares.append((bbox, approx))
                cv2.drawContours(frame, [approx], -1, (0,255,0), 2)

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

            # Sort left to right, then group into 3 columns
            cells.sort(key=lambda c: c['cx'])
            cols = [cells[i*3:(i+1)*3] for i in range(3)]

            # Sort each column top to bottom
            for col in cols:
                col.sort(key=lambda c: c['cy'])

            # Label squares with index
            for col_idx, col in enumerate(cols):
                for row_idx, cell in enumerate(col):
                    idx = col_idx * 3 + row_idx
                    x, y, w, h = cell['bbox']
                    cv2.putText(
                        frame,
                        str(idx),
                        (int(x), int(y) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,
                        (255,255,255),
                        2
                    )

            # Display layout help
            cv2.putText(frame, "Layout: 0 3 6 / 1 4 7 / 2 5 8",
                        (10, frame.shape[0] - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)

            # Capture colors every COOLDOWN seconds
            now = time()
            if now - last_capture >= COOLDOWN:
                color_matrix = [['' for _ in range(3)] for _ in range(3)]
                for col_idx, col in enumerate(cols):
                    for row_idx, cell in enumerate(col):
                        bbox = cell['bbox']
                        avg = get_avg_color(frame, bbox)
                        color = get_basic_color(avg)
                        color_matrix[row_idx][col_idx] = color

                print("Detected Color Matrix:")
                for row in color_matrix:
                    print(row)
                last_capture = now

        cv2.imshow('Square Detection', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
