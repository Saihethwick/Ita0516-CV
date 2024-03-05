import cv2
import numpy as np
img = cv2.imread('C:/Users/saihe/OneDrive/Desktop/cv/images.jpeg')
input_points = np.float32([[56,65], [368,52], [28,387], [389,390]])
output_points = np.float32([[0,0], [300,0], [0,300], [300,300]])
matrix = cv2.getPerspectiveTransform(input_points, output_points)
output_image = cv2.warpPerspective(img, matrix, (300,300))
cv2.imshow("Input Image", img)
cv2.imshow("Output Image", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
