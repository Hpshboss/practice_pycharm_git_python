import numpy as np
import cv2 as cv
import os
import sys

img = cv.imread("temp.png", cv.IMREAD_COLOR)
tick1 = cv.getTickCount()
for i in range(5, 49, 2):
    img1 = cv.medianBlur(img, i)
tick2 = cv.getTickCount()
time = (tick2 - tick1)/cv.getTickFrequency()
print(time)
cv.imshow("hello image", img)
print(len(img))
px = img[0, 0]
print(px)
cv.namedWindow("hello image", cv.WINDOW_NORMAL)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("copy_temp.png", img)

array = [[1, 2], [3, 4]]
print(array[1][0])
print(len(array))
