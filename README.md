# 🖐️ PWM Control with Computer Vision 🤖

Control **PWM (Pulse Width Modulation)** using hand gestures! This project combines **Computer Vision** (OpenCV + MediaPipe) with an **Arduino** to adjust PWM signals based on the number of fingers you show to the camera.

<div style="display: flex; align-items: center;">
  <img src="https://github.com/William-Souza-Santos/PWM-Control-With-Computer-Vision/raw/main/Animation.gif" width="520" height="800">
  <img src="https://github.com/William-Souza-Santos/PWM-Control-With-Computer-Vision/raw/main/Arduino.gif" width="300" height="800">
</div>
---
---

## ✨ Features
- 👆 Detect hand gestures using your webcam.
- 📊 Convert finger count to PWM % (0%, 20%, 40%, 60%, 80%, 100%).
- 🔌 Send PWM values to Arduino via serial communication.
- 💡 Visual feedback on screen (PWM % and progress bar).

---

## 📦 Prerequisites
- 🐍 Python 3.x
- 📚 Libraries: `opencv-python`, `mediapipe`, `pyserial`
- 🔌 Arduino Board (Uno, Nano, etc.)
- 💻 Arduino IDE

---

## 🛠️ Installation

### 1. Install Python Libraries
```bash
pip install opencv-python mediapipe pyserial

```

### Mediapipe Hands Map
<img src="https://github.com/William-Souza-Santos/PWM-Control-With-Computer-Vision/blob/main/mediapipe_hands.jpg">

