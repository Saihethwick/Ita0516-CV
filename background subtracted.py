import cv2
import numpy as np
def subtract_background(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,binary_mask = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)
    inverted_mask = cv2.bitwise_not(binary_mask)
    result = cv2.bitwise_and(image, image, mask=inverted_mask)
    return result
def main():
    input_image = cv2.imread("C:/Users/saihe/OneDrive/Desktop/cv/WhatsApp Image 2024-02-22 at 21.05.49_559d2bc2.jpg")
    background_subtracted_image = subtract_background(input_image)
    cv2.imshow("Original Image", input_image)
    cv2.imshow("Background Subtracted Image", background_subtracted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
