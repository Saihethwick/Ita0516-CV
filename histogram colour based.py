import cv2
import numpy as np
import matplotlib.pyplot as plt
def analyze_histogram(image_path):
    img = cv2.imread(image_path)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist_hue = cv2.calcHist([hsv_img], [0], None, [180], [0, 180])
    hist_saturation = cv2.calcHist([hsv_img], [1], None, [256], [0, 256])
    hist_value = cv2.calcHist([hsv_img], [2], None, [256], [0, 256])
    plt.figure(figsize=(10, 5))
    plt.subplot(131)
    plt.plot(hist_hue, color='r')
    plt.title('Hue Histogram')
    plt.xlim([0, 180])
    plt.subplot(132)
    plt.plot(hist_saturation, color='g')
    plt.title('Saturation Histogram')
    plt.xlim([0, 256])
    plt.subplot(133)
    plt.plot(hist_value, color='b')
    plt.title('Value Histogram')
    plt.xlim([0, 256])
    plt.tight_layout()
    plt.show()
image_path = 'C:/Users/saihe/OneDrive/Desktop/cv/images.jpeg' 
analyze_histogram(image_path)
