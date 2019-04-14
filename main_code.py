import cv2


img1 = cv2.imread("apple_pencil.jpg")
img2 = cv2.imread("apple_pencil_plus.jpg")

add = img1 + img2

cv2.imshow("add", add)
cv2.waitKey(0)
cv2.destroyAllWindows()



