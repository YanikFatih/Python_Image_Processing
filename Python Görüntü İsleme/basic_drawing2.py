import cv2

img = cv2.imread("forest.png")
cv2.circle(img, (300,300), 70, (0, 255, 0), 3)
cv2.imshow("Circle", img)
cv2.waitKey(0)
# resmin belirlenen konumunda merkezli verilen değerlerde bir çember çizilir.
# thickness değeri -1 olarak verilirse içi dolu bir daire çizilir.