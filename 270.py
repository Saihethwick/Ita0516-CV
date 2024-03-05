import cv2
img = cv2.imread('C:/Users/saihe/OneDrive/Desktop/cv/images.jpeg')
img_cw_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Orginal", img)
cv2.imshow("Image rotated by 270 degree", img_cw_270)
cv2.waitKey(0)
cv2.destroyAllWindows()
