import cv2
import numpy as np

view = cv2.imread("forest.png")

print(view)

cv2.imshow("View", view)
cv2.waitKey(0)