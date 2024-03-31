import cv2
from compare_pose import match_pose
from add_text_to_frame import add_detected_text


def make_result(video_path,img,threshold=0.99):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()

    output_path = 'detected_video.mp4'  
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'H264')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    pose_image = match_pose(img)
    while True:
        ret, frame = cap.read()
        if not ret:
            break  
        if pose_image.compare_images(frame, threshold):
            frame = add_detected_text(frame)
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return output_path

