import cv2
import numpy as np

img = cv2.imread("imori.jpg").astype(np.float)
H, W, C = img.shape
red = img[:, :, 2].copy()
green = img[:, :, 1].copy()
blue = img[:, :, 0].copy()

out = 0.2126 * red + 0.7152 * green + 0.0722 * blue
out = out.astype(np.uint8)

# Determine threshold of Otsu's binarization
max_sigma = 0
max_t = 0

for _t in range(1, 255):
    v0 = out[np.where(out < _t)]
    m0 = np.mean(v0) if len(v0) > 0 else 0.
    w0 = len(v0) / (H * W)
    v1 = out[np.where(out >= _t)]
    m1 = np.mean(v1) if len(v1) > 0 else 0.
    w1 = len(v1) / (H * W)
    sigma = w0 * w1 * ((m0 - m1) ** 2)
    if sigma > max_sigma:
        max_sigma = sigma
        max_t = _t

print("threshold >>", max_t)
threshold = max_t
out[out < threshold] = 0
out[out >= threshold] = 255

cv2.imwrite("outQ4.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
