import cv2
import numpy as np
image = cv2.imread('C:/Users/saihe/OneDrive/Desktop/cv/me.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
model = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'res10_300x300_ssd_iter_140000_fp16.caffemodel')
for (x, y, w, h) in faces:
    face = gray[y:y+h, x:x+w]
    face = cv2.resize(face, (300, 300))
    confidences = model.forward()
    i = np.argmax(confidences)
    if confidences[i] > 0.5:
        label = "Smiling"
    else:
        label = "Not Smiling"
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
