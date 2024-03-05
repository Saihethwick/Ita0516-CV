import cv2
import numpy as np
img = cv2.imread('C:/Users/saihe/OneDrive/Desktop/cv/images.jpeg')
rows, cols, _ = img.shape
M = np.float32([[1, 0.5, 0], [0, 1, 0]])
img_transformed = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow("Transformed Image", img_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
