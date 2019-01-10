import cv2

img = cv2.imread("imori.jpg")
red = img[:, :, 2].copy()
green = img[:, :, 1].copy()
blue = img[:, :, 0].copy()

img[:, :, 2] = blue
img[:, :, 1] = green
img[:, :, 0] = red

cv2.imwrite("outQ1.jpg", img)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
