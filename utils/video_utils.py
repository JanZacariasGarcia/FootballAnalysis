import cv2

def read_video(video_path):
    #24fps
    cap = cv2.VideoCapture(video_path) #video capture object
    frames = []
    while True:
        ret, frame = cap.read() #ret is a flag, if there is no frame, ie. the video has ended, flag is raised and loop break
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, 
                          (output_video_frames[0].shape[1], output_video_frames[0].shape[0])) #path,format,fps, h*w
    for frame in output_video_frames:
        out.write(frame)
    out.release()