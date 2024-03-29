import cv2
import numpy as np
image = cv2.imread('C:/Users/saihe/OneDrive/Desktop/cv/images.jpeg', 0) 
kernel = np.ones((5, 5), np.uint8) 
opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
top_hat = cv2.subtract(image, opened_image)
cv2.imshow('Original Image', image)
cv2.imshow('Top Hat Image', top_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
