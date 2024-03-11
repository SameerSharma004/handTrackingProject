import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
sWidth, sHeight = 1920, 1080
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center= (x, y), radius=15, color=(255,0,255))
                    index_x = sWidth/frame_width*x
                    index_y = sHeight/frame_height*y
                    pyautogui.moveTo(x, y)
                if id == 4:
                    cv2.circle(img=frame, center= (x, y), radius=15, color=(255,0,255))
                    thumb_x = sWidth/frame_width*x
                    thumb_y = sHeight/frame_height*y
                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow('Image', frame)
    cv2.waitKey(1)