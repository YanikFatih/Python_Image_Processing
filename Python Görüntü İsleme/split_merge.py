import cv2
import numpy as np

image = cv2.imread('green.png')
b, g, r = cv2.split(image)
zero_matrix = np.zeros(image.shape[:2], np.uint8)
blue = cv2.merge([b, zero_matrix, zero_matrix])
green = cv2.merge([zero_matrix, g, zero_matrix])
red = cv2.merge([zero_matrix, zero_matrix, r])
cv2.imshow("Original", image)
cv2.imshow("B", blue)
cv2.imshow("G", green)
cv2.imshow("R", red)
cv2.waitKey(0)