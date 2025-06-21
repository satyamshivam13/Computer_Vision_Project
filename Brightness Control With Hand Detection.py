import cv2
import mediapipe as mp
import numpy as np
from math import hypot
import screen_brightness_control as sbc

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=1
)
mp_draw = mp.solutions.drawing_utils

# Start video capture
cap = cv2.VideoCapture(0)

def calculate_brightness(thumb_tip, index_tip):
    x1, y1 = thumb_tip
    x2, y2 = index_tip
    length = hypot(x2 - x1, y2 - y1)
    brightness = np.interp(length, [15, 220], [0, 100])
    return brightness

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    landmark_list = []

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            h, w, _ = frame.shape
            for id, lm in enumerate(hand_landmarks.landmark):
                x, y = int(lm.x * w), int(lm.y * h)
                landmark_list.append((id, x, y))
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if landmark_list:
        thumb_tip = (landmark_list[4][1], landmark_list[4][2])
        index_tip = (landmark_list[8][1], landmark_list[8][2])

        cv2.circle(frame, thumb_tip, 8, (0, 255, 0), cv2.FILLED)
        cv2.circle(frame, index_tip, 8, (0, 255, 0), cv2.FILLED)
        cv2.line(frame, thumb_tip, index_tip, (0, 255, 0), 2)

        brightness_level = calculate_brightness(thumb_tip, index_tip)
        sbc.set_brightness(int(brightness_level))

    cv2.imshow("Hand Brightness Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
