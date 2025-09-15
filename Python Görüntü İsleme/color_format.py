import cv2

view = cv2.imread("forest.png")
grey = cv2.cvtColor(view, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(view, cv2.COLOR_BGR2RGB)

cv2.imshow("grey", grey)
cv2.imshow("Original View", view)
cv2.imshow("RGB", rgb)
cv2.waitKey(0)