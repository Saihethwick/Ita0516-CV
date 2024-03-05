import cv2
def play_video_in_reverse(video_path):
    video = cv2.VideoCapture("C:/Users/saihe/OneDrive/Desktop/cv/okk.mp4")
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    for frame_number in range(total_frames - 1, -1, -1):
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = video.read()
        if ret:
            cv2.imshow('Video in Reverse', frame)
            cv2.waitKey(30)  
        else:
            print("Error reading frame")
    video.release()
    cv2.destroyAllWindows()

def main():
    video_path = "input_video.mp4"
    play_video_in_reverse(video_path)

if __name__ == "__main__":
    main()
