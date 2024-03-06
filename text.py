import numpy as np
import cv2
def create_white_image(size):
    image = np.ones((size, size, 3), dtype=np.uint8) * 255
    return image
def draw_text(image, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(0, 0, 0), thickness=2):
    cv2.putText(image, text, position, font, font_scale, color, thickness)
def main():
    size = int(input("Enter the size of the image: "))
    white_image = create_white_image(size)
    text = input("Enter the text to be written on the image: ")
    text_position = (size // 4, size // 2)
    draw_text(white_image, text, text_position)
    cv2.imshow("White Image with Text", white_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
