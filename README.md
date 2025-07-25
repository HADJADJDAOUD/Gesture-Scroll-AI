# Gesture Scroll AI

**Gesture Scroll AI** lets you control your computer’s scrolling using hand gestures detected in real time by your webcam. It's built with Python, MediaPipe, and OpenCV, and supports customizable scroll speed, two-finger bend gestures, and fist-based continuous scrolling.
* you see that feeling when you are lazy to use the mouse or you want to move around the room or smthing and you can't access your mouse for scrolling for your book , now you can !!**SUUUUI**
---

## 🚀 Features

* **Thumb Bend**: Bend your thumb toward your palm to scroll **up**.
* **Fist Scroll**: Make a fist to trigger continuous scroll down.
* **Speed Control**: Adjust scroll speed on-the-fly via an OpenCV slider (1–500).
* **Landmark Labels**: Visualize hand landmarks (0–20) overlaid on video feed.

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/HADJADJDAOUD/Gesture-Scroll-Ai.git
   cd Gesture-Scroll-Ai
   ```
2. **Set up a virtual environment** (python version 3.7-3.11.)

   ```bash
   python3 -m venv venv
   # Windows
   venv\\Scripts\\activate
   # macOS/Linux
   source venv/bin/activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

> **requirements.txt** should contain:
>
> ```
> opencv-python
> mediapipe
> pyautogui
> ```

---

## ⚙️ Usage

1. Activate your virtual environment.
2. Run the script:

   ```bash
   python camera.py
   ```
3. A window titled **Gesture Scroll & Labels** will appear.
4. Use the **Speed** slider at the top to set your preferred scroll speed.
5. Perform gestures:

   * **Thumb bend** → scroll **up**.
   * **Fist** → continuous scroll **down**.
6. Press **`q`** to quit.

---

## 🛠 Configuration

* **`MAX_SPEED`** in `main.py` controls the maximum scroll speed (default 500).
* **`SCROLL_COOLDOWN`** controls the minimum time between scroll events (default 0.1s).
* Modify thresholds in helper functions (`is_finger_bent`, `is_thumb_bent_proximity`, `is_fist`) for sensitivity.

---

## ✨ Customization

* **Additional Gestures**: Integrate new gestures by adding detection functions and mapping to scroll actions.
* **Smoothness**: Experiment with `SCROLL_COOLDOWN` or introduce smoothing filters (e.g., Kalman filter) on landmark positions.
* **Web Integration**: Wrap this script in an Electron or Flask app to control web pages directly.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙋‍♂️ Contributing

1. Fork the repo.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: \`git commit -m "Add feature"
4. Push to the branch: `git push origin feature-name`
5. Open a Pull Request.

# SUUUUUUUUUUUUUUUUUUUUUUUUUI
