import numpy as np
import cv2


img = cv2.imread("temp.png", cv2.IMREAD_COLOR)
px = img[55, 55]
print(px)

roi = img[100:150, 100:150]
print(roi)

img[100:150, 100:150] = [255, 255, 255]


cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

