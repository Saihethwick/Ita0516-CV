import numpy as np
import cv2
def create_colored_boxes_image(size):
    image = np.ones((size, size, 3), dtype=np.uint8) * 255
    box_size = size // 10
    colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]    
    for i in range(4):
        x = i // 2 * (size - box_size)
        y = i % 2 * (size - box_size)
        image[x:x+box_size, y:y+box_size] = colors[i]
    return image
size = int(input("Enter the size of the image: "))
image = create_colored_boxes_image(size)
cv2.imshow("Colored Boxes Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
