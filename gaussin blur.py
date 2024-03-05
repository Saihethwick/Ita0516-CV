import cv2
image_path = "C:/Users/saihe/OneDrive/Desktop/cv/images.jpeg" 
image = cv2.imread(image_path)
if image is None:
    print("Error: Unable to read the image.")
    exit()
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
