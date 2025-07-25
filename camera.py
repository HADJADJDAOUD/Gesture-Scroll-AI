# Gesture Scroll with Two-Finger Bending Control & Fist Scroll & Landmark Labels (Speed Control)
# ------------------------------------------------

import cv2
import mediapipe as mp
import pyautogui
import math
import time


MAX_SPEED = 500  # Increase this to allow faster scrolling
SCROLL_COOLDOWN = 0.05  # seconds between scroll events



def is_finger_bent(landmarks, tip_id, pip_id, threshold=0.02):
    """
    Detects if a finger is bent by comparing the tip and pip landmark y-coordinates.
    """
    return (landmarks[tip_id].y - landmarks[pip_id].y) > threshold


def is_thumb_bent_proximity(landmarks, target_ids=(17, 13, 9), distance_thresh=0.05):
    """
    Detects thumb bend by measuring distance between thumb tip (4) and other finger landmarks.
    """
    thumb_tip = landmarks[4]
    for tid in target_ids:
        point = landmarks[tid]
        dx, dy, dz = thumb_tip.x - point.x, thumb_tip.y - point.y, thumb_tip.z - point.z
        if math.sqrt(dx*dx + dy*dy + dz*dz) < distance_thresh:
            return True
    return False


def is_fist(landmarks, threshold=0.05):
    """
    Detects a fist by checking if all fingertips are close to their respective MCP landmarks.
    Fingertip IDs: 4, 8, 12, 16, 20
    MCP IDs:      2, 5, 9, 13, 17
    """
    tip_ids = [4, 8, 12, 16, 20]
    mcp_ids = [2, 5, 9, 13, 17]
    for tip, mcp in zip(tip_ids, mcp_ids):
        dx = landmarks[tip].x - landmarks[mcp].x
        dy = landmarks[tip].y - landmarks[mcp].y
        dz = landmarks[tip].z - landmarks[mcp].z
        if math.sqrt(dx*dx + dy*dy + dz*dz) > threshold:
            return False
    return True

# ------------------------------------------------
# Main Function
# ------------------------------------------------
def main():
    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    )
    mp_draw = mp.solutions.drawing_utils

  
    window_name = 'Gesture Scroll & Labels'
    cv2.namedWindow(window_name)
    cv2.createTrackbar('Speed', window_name, 20, MAX_SPEED, lambda x: None)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    print("Gesture Scroll with Fist & Two-Finger Control Active. Press 'q' to quit.")
    last_scroll_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

    
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get speed from trackbar, enforce minimum of 1
        speed = cv2.getTrackbarPos('Speed', window_name)
        if speed < 1:
            speed = 1

        results = hands.process(rgb)
        if results.multi_hand_landmarks:
            landmarks = results.multi_hand_landmarks[0].landmark
            mp_draw.draw_landmarks(frame, results.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)

            # Label landmarks
            for idx, lm in enumerate(landmarks):
                x_px, y_px = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (x_px, y_px), 3, (0,255,0), -1)
                cv2.putText(frame, str(idx), (x_px+5, y_px-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,0,0), 1)

            # Detect gestures
            fist = is_fist(landmarks)
            thumb_bent = is_thumb_bent_proximity(landmarks)
            index_bent = is_finger_bent(landmarks, tip_id=8, pip_id=6)

            current_time = time.time()
            if current_time - last_scroll_time > SCROLL_COOLDOWN:
                if fist:
                    # Fist -> continuous scroll down
                    pyautogui.scroll(-speed)
                    last_scroll_time = current_time
                elif thumb_bent and not index_bent:
                    # Thumb bend -> scroll up
                    pyautogui.scroll(speed)
                    last_scroll_time = current_time
                elif index_bent and not thumb_bent:
                    # Index bend -> scroll down
                    pyautogui.scroll(-speed)
                    last_scroll_time = current_time

        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
