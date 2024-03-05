import cv2
image_path = "C:/Users/saihe/OneDrive/Desktop/cv/images.jpeg" 
image = cv2.imread(image_path)
if image is None:
    print("Error: Unable to read the image.")
    exit()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny_edges = cv2.Canny(gray_image, 50, 150) 
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', canny_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
