import cv2
import numpy as np
import math

# -------- Function: Detect Shape --------
def detect_shape(approx):
    sides = len(approx)
    if sides == 3:
        return "Triangle"
    elif sides == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        if 0.95 <= aspect_ratio <= 1.05:
            return "Square"
        else:
            return "Rectangle"
    elif sides == 5:
        return "Pentagon"
    elif sides > 5:
        return "Circle"
    return "Unknown"

# -------- Function: Find Center of Contour --------
def find_center(contour):
    M = cv2.moments(contour)
    if M["m00"] == 0:
        return None
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    return (cx, cy)

# -------- Function: Calculate Distances --------
def calculate_distances(frame, centers, labels):
    pixels_per_cm = 37.79  # <-- Replace this with your own calibrated value!

    for i in range(len(centers)):
        for j in range(i+1, len(centers)):
            if labels[i] == labels[j]:  # Only compare same shapes
                c1 = centers[i]
                c2 = centers[j]

                # Distance in pixels
                pixel_dist = math.hypot(c2[0] - c1[0], c2[1] - c1[1])

                # Convert to centimeters
                dist_cm = pixel_dist / pixels_per_cm
                midpoint = ((c1[0]+c2[0])//2, (c1[1]+c2[1])//2)

                # Draw line & display distance
                cv2.line(frame, c1, c2, (0, 255, 0), 2)
                cv2.putText(frame, f"{dist_cm:.2f} cm", midpoint,
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

# -------- Main Webcam Processing Loop --------
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    centers = []
    labels = []

    # Preprocessing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 1)
    edges = cv2.Canny(blur, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 400:  # Filter small shapes
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            shape = detect_shape(approx)
            center = find_center(cnt)

            if center:
                centers.append(center)
                labels.append(shape)
                cv2.drawContours(frame, [approx], 0, (255, 0, 0), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
                cv2.putText(frame, shape, (center[0]+10, center[1]),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    calculate_distances(frame, centers, labels)

    cv2.imshow("Shape Detection with Distance in CM", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
