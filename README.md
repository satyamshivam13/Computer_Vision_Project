# Gesture-Based Brightness Controller

This repository contains a Python application that adjusts your computer’s screen brightness using **hand gestures** detected via a webcam. The project leverages **MediaPipe** and **OpenCV** for real-time hand tracking and gesture interpretation, offering a seamless and intuitive brightness control interface.

## ✨ Features

- **Real-time Hand Tracking**: Detects hand landmarks using MediaPipe.
- **Gesture-Based Brightness Control**: Adjusts brightness based on the distance between your thumb and index finger.
- **Cross-Compatible**: Works on most systems with a webcam and brightness control API.
- **Simple & Lightweight**: Clean Python implementation with minimal dependencies.

## 🛠️ Technologies Used

- **Python 3.7+**
- **OpenCV** – Real-time video processing
- **MediaPipe** – Robust hand tracking
- **Screen Brightness Control** – Cross-platform brightness adjustment (`screen-brightness-control`)

## 📦 Prerequisites

Ensure the following are installed:

- Python 3.7 or later
- Webcam
- Required Python packages (listed in `requirements.txt`)

To install dependencies:

```bash
pip install -r requirements.txt
```

> Note: If you’re using Linux, `screen-brightness-control` may require `xrandr` or `ddcutil`. On Windows, it works out of the box for most laptops and monitors.

## 🚀 Getting Started

1. Clone this repository:

```bash
git clone https://github.com/satyamshivam13/Gesture_Brightness_Control.git
cd Gesture_Brightness_Control
```

2. Run the application:

```bash
python main.py
```

3. Show your hand to the webcam. The app will track the position of your thumb and index finger.

- Move them **closer together** to reduce brightness.
- Move them **farther apart** to increase brightness.

4. Press `q` to exit.

## 📁 Project Structure

```
Gesture_Brightness_Control/
├── main.py                # Main application script
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── assets/                # (Optional) Images, screenshots, videos
```

## ⚙️ Customization

- Change gesture sensitivity by adjusting interpolation range in `main.py`.
- Limit max/min brightness levels as needed.
- Extend to more gestures or multiple hands by modifying the detection logic.

## 🤝 Contributions

Contributions are welcome! To contribute:

1. Fork the repo.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for hand tracking
- [OpenCV](https://opencv.org/) for video processing
- [screen-brightness-control](https://pypi.org/project/screen-brightness-control/) for system brightness handling

---

**Contact:**  
For any questions or support, feel free to [open an issue](https://github.com/your-username/Gesture_Brightness_Control/issues) or email: `shivamsatyam35@gmail.com`.

Enjoy gesture-based brightness control! 🌟