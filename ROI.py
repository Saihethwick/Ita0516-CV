import cv2
image = cv2.imread('C:/Users/saihe/OneDrive/Desktop/cv/images.jpeg')
x1, y1 = 100, 100
x2, y2 = 300, 300 
roi = image[y1:y2, x1:x2]
cv2.imshow('original',image)
cv2.waitKey(0)
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('cropped_roi.jpg', roi)
