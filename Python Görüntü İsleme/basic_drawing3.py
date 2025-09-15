import cv2

img = cv2.imread("forest.png")
cv2.rectangle(img,(300,300),(600,500),(255,255,255),4)
cv2.imshow("Rectangle", img)
cv2.waitKey(0)
