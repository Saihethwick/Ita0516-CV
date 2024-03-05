import cv2
import pytesseract
def extract_text_from_video(video_path):
    video = cv2.VideoCapture("C:/Users/saihe/OneDrive/Desktop/cv/text vi.mp4")
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    while True:
        ret, frame = video.read()
        if not ret:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray_frame)
        print(text)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()
def main():
    video_path = "input_video.mp4"
    extract_text_from_video(video_path)
if __name__ == "__main__":
    main()
