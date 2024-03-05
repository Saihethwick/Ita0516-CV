import cv2
def resize_image(image_path, scale_percent=None, new_width=None, new_height=None):
    img = cv2.imread(image_path)
    if scale_percent is not None:
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
    else:
        width = new_width
        height = new_height
    resized_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    cv2.imshow('Original Image', img)
    cv2.imshow('Resized Image', resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_path = 'C:/Users/saihe/OneDrive/Desktop/cv/images.jpeg'  
resize_image(image_path, scale_percent=150)
resize_image(image_path, new_width=200, new_height=200)
