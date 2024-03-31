import cv2

def add_detected_text(frame):
    # setting the type of font and the text to be displayed
    text = "Detected"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    font_color = (0, 255, 0)  
    thickness = 2
    margin = 10

    # Get the size of the text box
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_x = frame.shape[1] - text_size[0] - margin
    text_y = text_size[1] + margin
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, font_color, thickness)
    return frame