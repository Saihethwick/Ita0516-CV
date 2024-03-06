import cv2
import numpy as np
image = cv2.imread('C:/Users/saihe/OneDrive/Desktop/cv/WhatsApp Image 2024-02-22 at 21.05.49_559d2bc2.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
lower_threshold = 100
upper_threshold = 200
binary_image = cv2.inRange(gray_image, lower_threshold, upper_threshold)
cv2.imshow('Segmented Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
