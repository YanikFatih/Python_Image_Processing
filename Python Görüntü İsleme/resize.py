import cv2
import numpy as np

image = cv2.imread("forest.png")
new_size = cv2.resize(image, (1280, 720)) #width - height

cv2.imshow("Original", image)
cv2.imshow("New Size", new_size)
cv2.waitKey(0)