import cv2
import numpy as np
img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
ret, corners = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)
corners = np.uint8(np.where(ret == 255))
for corner in corners:
    cv2.circle(img, (corner[0], corner[1]), 5, (0, 0, 255), -1)
cv2.imshow('Image with corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
