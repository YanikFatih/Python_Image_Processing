import cv2

webcam = cv2.VideoCapture(0) #0 olarak tanımladıgımız zaman otomatik olarak webcam bulunur ve açılır (değişebilir 1 2 vs)

#video mantığıyla bir while true döngüsü
while True:
    control, videoMatris = webcam.read()
    grey = cv2.cvtColor(videoMatris, cv2.COLOR_BGR2GRAY) #siyah beyaz formata dönüştürme işlemi
    cv2.imshow("Webcam", grey)
    if cv2.waitKey(10) == 27: break