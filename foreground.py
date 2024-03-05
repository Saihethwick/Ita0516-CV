import cv2
import numpy as np
def subtract_foreground(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_mask = cv2.threshold(gray_image, 10, 255, cv2.THRESH_BINARY)
    result = cv2.bitwise_and(image, image, mask=binary_mask)
    return result
def main():
    input_image = cv2.imread("C:/Users/saihe/OneDrive/Desktop/cv/images.jpeg")
    foreground_subtracted_image = subtract_foreground(input_image)
    cv2.imshow("Original Image", input_image)
    cv2.imshow("Foreground Subtracted Image", foreground_subtracted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
