import cv2
def count_faces(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return len(faces)
def main():
    image_path = "C:/Users/saihe/OneDrive/Desktop/cv/WhatsApp Image 2024-02-22 at 21.05.49_559d2bc2.jpg"
    num_faces = count_faces(image_path)
    print("Number of faces detected:", num_faces)
if __name__ == "__main__":
    main()
