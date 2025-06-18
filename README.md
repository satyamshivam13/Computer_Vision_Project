Brightness Control With Hand Detection

Welcome to the Brightness Control With Hand Detection project! This repository contains a Python-based application that adjusts your computer’s screen brightness using hand gestures detected through a webcam. The project leverages computer vision techniques and machine learning models to create a seamless and intuitive user experience.

Features

	•	Real-time Hand Detection: Uses a webcam to detect hand gestures.
	•	Brightness Control: Adjusts screen brightness based on the distance between fingers.
	•	User-friendly: Lightweight and easy to use.
	•	Customizable: Modify gesture mappings and thresholds as needed.

Technologies Used

	•	Python: Programming language.
	•	OpenCV: For image and video processing.
	•	Mediapipe: For hand tracking and gesture recognition.
	•	PyAutoGUI: For controlling screen brightness.

Prerequisites

Before running the project, ensure you have the following installed:
	•	Python 3.7 or later
	•	Required Python packages (see requirements.txt)

Installation

	1.	Clone the repository:

git clone https://github.com/satyamshivam13/Computer_Vision_Project

cd Brightness-Control-With-Hand-Detection


	2.	Install dependencies:

pip install -r requirements.txt


	3.	Ensure your webcam is functional.

Usage

	1.	Run the main script:

python main.py


	2.	Position your hand in front of the webcam. The application will track your hand and adjust the brightness based on the gesture.
	•	Example Gesture: Use your thumb and index finger to control the brightness. The distance between them determines the brightness level.
	3.	Exit the program by pressing q.

Project Structure

Brightness-Control-With-Hand-Detection/
├── main.py                # Main application script
├── requirements.txt       # Required Python packages
├── README.md              # Project documentation
├── utils/                 # Helper functions and modules
├── models/                # Pre-trained models (if applicable)
└── assets/                # Images and other resources

Customization

	•	Modify the hand gesture mappings in main.py to suit your preferences.
	•	Adjust sensitivity and thresholds to fine-tune brightness control in the settings.

Contributions

Contributions are welcome! Please follow these steps:
	1.	Fork the repository.
	2.	Create a new branch for your feature or bug fix.
	3.	Commit your changes and submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

	•	Mediapipe for robust hand tracking.
	•	OpenCV for video and image processing.
	•	PyAutoGUI for controlling system-level brightness.

Contact

For questions or feedback, feel free to reach out via email: shivamsatyam35@gmail.com or open an issue in the repository.

Enjoy using Brightness Control With Hand Detection and make your screen adjustment as simple as a wave!
