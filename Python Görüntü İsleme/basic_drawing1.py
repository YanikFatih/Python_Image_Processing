import cv2

image = cv2.imread("forest.png")
cv2.line(image, (50,50), (250, 350), (0, 0, 255), 5)
cv2.imshow("Line", image)
cv2.waitKey(0)