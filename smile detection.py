import cv2
smile_cascade =cv2.CascadeClassifier("C:/Users/saihe/OneDrive/Desktop/cv/haarcascade_smile.xml")
image = cv2.imread('C:/Users/saihe/OneDrive/Desktop/cv/face-match.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
smiles = smile_cascade.detectMultiScale(gray, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25))
for (x, y, w, h) in smiles:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('Smile Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

