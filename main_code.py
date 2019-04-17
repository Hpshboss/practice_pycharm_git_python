import cv2


img1 = cv2.imread("apple_pencil.jpg")
img2 = cv2.imread("apple_pencil_plus.jpg")

# add = img1 + img2
# add = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
rows, cols, channels = img2.shape
rol = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()



