import cv2
import numpy as np

img = cv2.imread("imori.jpg").astype(np.float)
H, W, C = img.shape
red = img[:, :, 2].copy()
green = img[:, :, 1].copy()
blue = img[:, :, 0].copy()

out = 0.2126 * red + 0.7152 * green + 0.0722 * blue
out = out.astype(np.uint8)

max_t = max_val = 0

for t in range(0, 256):
    v0 = out[np.where(out < t)[0]]
    m0 = np.mean(v0) if len(v0) > 0 else 0
    w0 = len(v0) / (H * W)
    v1 = out[np.where(out >= t)[0]]
    m1 = np.mean(v1) if len(v1) > 0 else 0
    w1 = len(v1) / (H*W)

    result = w0 * w1 * ((m0 - m1) ** 2)
    if max_val < result:
        max_val = result
        max_t = t

print("threshold >>", max_t)
threshold = max_t
out[out < threshold] = 0
out[out >= threshold] = 255

cv2.imwrite("outQ4.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
