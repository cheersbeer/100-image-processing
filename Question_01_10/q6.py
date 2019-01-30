import cv2
import numpy as np

img = cv2.imread("imori.jpg")

out = img.copy()

'''
for i in range(4):
    ind = np.where(((64 * i - 1) <= out) & (out < (64 * (i + 1) - 1)))
    out[ind] = 32*(2*i+1)
'''

out = out // 64 * 64 + 32

cv2.imwrite("outQ6.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
