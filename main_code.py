import numpy as np
import cv2
import matplotlib.pyplot as plt

# img = cv2.imread("temp.png", cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
# IMREAD_GRAYSCALED = 0(default)
# IMREAD_UNCHANGED = -1
#
# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# plt.imshow(img, cmap="gray", interpolation="bicubic")
# plt.plot([50, 100], [80, 100], "c", linewidth=5)
# plt.show()
#
# cv2.imwrite("copy_temp.png", img)

cap = cv2.VideoCapture(1)

while True:
    print("check0")
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    print("check1")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()







