
#  Shape Distance Detector using OpenCV

This Python-based real-time application uses your webcam feed to detect common geometric shapes and measure the distance between identical shapes (in centimeters) using OpenCV. It overlays detected shape contours, center points, and distance lines on the live video feed. The application includes an easy calibration process to convert pixel distances into real-world units, ensuring accurate measurements.

---

## 🎯 Features

* **Shape detection:** Identifies geometric shapes such as Circle, Square, Rectangle, Triangle, and Pentagon.
* **Real-time distance calculation:** Computes distances (in cm) between matching shapes on the fly.
* **Live video overlay:** Displays the webcam feed with contours drawn around shapes, center points marked, and distance lines annotated.
* **Easy calibration:** Simple process to calibrate pixel-to-cm conversion factor for accurate measurements.
* **Center point labeling:** Marks the centroid of each detected shape and labels them by shape type.

## 🛠️ Tech Stack

* **Python 3**
* **OpenCV** (cv2)
* **NumPy**
* **math** (built-in Python module)

---

## 🚀 Getting Started

### ✅ Prerequisites

* Python 3.x installed on your system.
* A webcam connected to your computer.

### ✅ Installation

```bash
git clone https://github.com/agamsiingh/shape-distance-detector.git
cd shape-distance-detector
pip install opencv-python numpy
```

### ✅ Run the Project

```bash
python shape_distance_detector.py
```

*Press `ESC` to exit the webcam window.*

---

## 🧪 Calibration Guide (Important!)

To convert pixel measurements to **real-world centimeters**, calibrate your setup as follows:

1. Place a **ruler or a known object** (e.g., 10 cm long) in view of your webcam.
2. Measure how many **pixels** correspond to that known length.
3. Update the calibration factor in the code. For example:

   ```python
   pixels_per_cm = 37.79  # Replace with your measured value (e.g., 377.9 px for 10 cm)
   ```
4. Re-run the project using the updated value. This ensures accurate cm distance measurements for your camera setup.

*Calibrate once for each new camera or distance setup to maintain accuracy.*

---

## 📂 Folder Structure

```
shape-distance-detector/
│
├── shape_distance_detector.py   # Main Python application
├── README.md                    # Project documentation (this file)
├── LICENSE                      # License file (MIT)
└── demo.gif / demo.png          # (Optional) Demo visualization
```

---

## 🧠 Future Improvements

* Auto-calibration using markers or QR codes for automatic scaling.
* Export distance measurements and shape data to CSV files.
* Add bounding box dimensions (width/height) in cm for each detected shape.
* Support additional shapes and improved detection accuracy.

---

## 📸 Demo
Images 
<img width="597" height="407" alt="Image" src="https://github.com/user-attachments/assets/a9b24fcf-7d39-4b0a-a8df-4fbfa703c03d" />
<img width="609" height="194" alt="Image" src="https://github.com/user-attachments/assets/6566740e-313c-4daf-b50a-355ac6fbf2db" />
<img width="604" height="398" alt="Image" src="https://github.com/user-attachments/assets/840aa474-6f69-4c64-aa18-82837acd2317" />
<img width="395" height="442" alt="Image" src="https://github.com/user-attachments/assets/9139240f-dc1d-4eaf-892d-5e53db5048ea" />

Videos
https://github.com/user-attachments/assets/5553e6e5-c3fb-4a0e-bd79-bc564e4384e4
https://github.com/user-attachments/assets/bda6e78e-3511-4303-9b23-2c2e6a4be917


---

## 👤 Author

**Agam Singh**
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/agam-singh-b34310246/).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

