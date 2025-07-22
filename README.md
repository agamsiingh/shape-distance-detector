
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
* Measure distances between different types of shapes.
* Add bounding box dimensions (width/height) in cm for each detected shape.
* Support additional shapes and improved detection accuracy.

---

## 📸 Demo
<!-- Uploading "Screenshot 2025-07-22 134116.png"... -->


---

## 👤 Author

**Agam Singh**
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/agam-singh-b34310246/).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

