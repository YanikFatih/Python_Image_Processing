import cv2
import mediapipe as mp

video = cv2.VideoCapture("video name should be here")
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

with mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while True:
        control, frame = video.read()
        if control == False:
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb)
        if results.pose_landmarks:
            mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        cv2.imshow("3D Detection", frame)
        if cv2.waitKey(10) == 27:
            break

video.release()
cv2.destroyAllWindows()