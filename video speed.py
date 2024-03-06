import cv2
def play_video(video_path, speed=1.0):
    cap = cv2.VideoCapture("C:/Users/saihe/OneDrive/Desktop/cv/okk.mp4")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video', frame)
        cv2.waitKey(int(1000 / (25 * speed)))  
    cap.release()
    cv2.destroyAllWindows()
video_path = 'captured_video.mp4'
print("Playing video normally...")
play_video(video_path)
print("\nPlaying video in slow motion...")
play_video(video_path, speed=0.5) 
print("\nPlaying video in fast motion...")
play_video(video_path, speed=2.0) 
