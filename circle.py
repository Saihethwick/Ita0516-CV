import numpy as np
import cv2
def create_white_image(size):
    image = np.ones((size, size, 3), dtype=np.uint8) * 255
    return image
def draw_circle(image, center, radius, color=(0, 0, 0), thickness=2):
    cv2.circle(image, center, radius, color, thickness)
def main():
    size = int(input("Enter the size of the image: "))
    white_image = create_white_image(size)
    center = (size // 2, size // 2)
    radius = min(size // 4, 100)
    draw_circle(white_image, center, radius)
    cv2.imshow("White Image with Circle", white_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
