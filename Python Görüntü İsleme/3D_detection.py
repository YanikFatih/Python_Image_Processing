import cv2
import mediapipe as mp
mp_3d = mp.solutions.objectron
mp_3d_draw = mp.solutions.drawing_utils
img = cv2.imread("sneaker.png")
img = cv2.resize(img, (600, 600))
with mp_3d.Objectron(static_image_mode = True, max_num_objects = 1, min_detection_confidence = 0.5, min_tracking_confidence = 0.5, model_name = "Shoe") as obj_3d:
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = obj_3d.process(rgb)
    if results.detected_objects:
        for detection in results.detected_objects:
            mp_3d_draw.draw_landmarks(img, detection.landmarks_2d, mp_3d.BOX_CONNECTIONS, mp_3d_draw.DrawingSpec((255, 0, 0), 10, 6), mp_3d_draw.DrawingSpec((0, 255, 0), 4))
    cv2.imshow("3D Detection", img)
    cv2.waitKey(0)