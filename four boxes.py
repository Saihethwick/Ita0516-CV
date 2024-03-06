import numpy as np
import cv2
def create_image_with_boxes(size):
    image = np.ones((size, size, 3), dtype=np.uint8) * 255
    box_size = size // 10
    image[:box_size, :box_size] = [0, 0, 0]
    image[:box_size, -box_size:] = [255, 0, 0]
    image[-box_size:, :box_size] = [0, 255, 0]
    image[-box_size:, -box_size:] = [0, 0, 255]
    return image
size = int(input("Enter the size of the image: "))
image_with_boxes = create_image_with_boxes(size)
cv2.imshow("Image with Boxes", image_with_boxes)
cv2.waitKey(0)
cv2.destroyAllWindows()
