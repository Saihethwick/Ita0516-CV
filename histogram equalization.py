import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = "C:/Users/saihe/OneDrive/Desktop/cv/images.jpeg" 
image = cv2.imread(image_path)
if image is None:
    print("Error: Unable to read the image.")
    exit()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized_image = cv2.equalizeHist(gray_image)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title('Equalized Image')
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')
plt.show()
