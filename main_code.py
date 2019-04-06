import numpy as np
import cv2 as cv

img = cv.imread("temp.png", 0)
cv.imshow("hello image", img)
cv.namedWindow("hello image", cv.WINDOW_NORMAL)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("copy_temp.png", img)
