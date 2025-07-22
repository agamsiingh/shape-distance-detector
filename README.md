
````markdown
# 🔷 Shape Distance Detector using OpenCV

This is a Python-based real-time application that uses your webcam to **detect geometric shapes** and **measure the distance between same shapes in centimeters** using OpenCV and contour detection.

---

## 🎯 Features

- 🧠 Shape detection: Circle, Square, Rectangle, Triangle, Pentagon
- 📏 Real-time distance calculation (in centimeters)
- 🎥 Live webcam feed with visual overlays
- 🧮 Easy calibration for accurate cm measurement
- 📌 Center point detection and labeling

---

## 📸 Demo

*(Add a screenshot or gif here once you have one)*

---

## 🛠️ Tech Stack

- Python 3
- OpenCV (cv2)
- NumPy
- Math module

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x installed
- Webcam connected

### ✅ Installation

```bash
git clone https://github.com/yourusername/shape-distance-detector.git
cd shape-distance-detector
pip install opencv-python numpy
````

### ✅ Run the Project

```bash
python shape_distance_detector.py
```

Press `ESC` to exit the webcam window.

---

## 🧪 Calibration Guide (Important!)

To convert pixel distances to **real-world centimeters**, follow these steps:

1. Place a **ruler or known object** (e.g. 10 cm) in front of your webcam.
2. Use OpenCV to measure how many **pixels** correspond to that known length.
3. Update this line in the code:

```python
pixels_per_cm = 37.79  # Replace with your actual value
```

If 10 cm = 377.9 pixels, then:
`pixels_per_cm = 377.9 / 10 = 37.79`

> 📏 Calibrate once for your camera + distance setup.

---

## 📂 Folder Structure

```
shape-distance-detector/
│
├── shape_distance_detector.py   # Main Python application
├── README.md                    # This file
├── demo.gif / demo.png          # (Optional) Demo visualization
```

---

## 🧠 Future Improvements

* Auto-calibration using QR code or marker
* Export measurements as CSV
* Detect and measure between different shapes
* Add bounding box dimensions in cm

---

## 👤 Author

**Agam Singh**
Feel free to connect:
🔗 [LinkedIn](https://www.linkedin.com/in/yourprofile)
📧 [your.email@example.com](mailto:your.email@example.com)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

```

---

### ✅ Next Steps

- Rename your Python file to: `shape_distance_detector.py`
- Add a screenshot or gif and name it `demo.gif` or `demo.png`
- Push your project to GitHub with the repo name:
```

shape-distance-detector

```

Would you like help creating the calibration script or generating a GIF demo for the README?
```
