import cv2

video = cv2.VideoCapture("car.mp4")

while True:
    control, videoMatris = video.read()
    cv2.imshow("Video", videoMatris)
    if cv2.waitKey(10) == 27: #27 ASCII tablosuna göre esc tuşunu temsil eder
        break