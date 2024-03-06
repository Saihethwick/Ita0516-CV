import cv2
original_image = cv2.imread('C:/Users/saihe/OneDrive/Desktop/cv/eye.jpg')
watermark_image = cv2.imread('C:/Users/saihe/OneDrive/Desktop/cv/water.png', cv2.IMREAD_UNCHANGED)
watermark_height, watermark_width, _ = watermark_image.shape
original_height, original_width, _ = original_image.shape
scale_factor = min(original_width / watermark_width, original_height / watermark_height)
resized_watermark = cv2.resize(watermark_image, (int(watermark_width * scale_factor), int(watermark_height * scale_factor)))
overlay = original_image.copy()
y_offset = original_height - resized_watermark.shape[0] - 10  
x_offset = original_width - resized_watermark.shape[1] - 10   
overlay[y_offset:y_offset+resized_watermark.shape[0], x_offset:x_offset+resized_watermark.shape[1]] = resized_watermark
if watermark_image.shape[2] == 4:
    alpha = resized_watermark[:, :, 3] / 255.0
    overlay = cv2.addWeighted(overlay, 1, resized_watermark[:, :, :3], 1, 0)
cv2.imshow('Watermarked Image', overlay)
cv2.waitKey(0)
cv2.destroyAllWindows()
