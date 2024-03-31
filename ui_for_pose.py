import streamlit as st
import cv2
import numpy as np
from get_video import make_result
import os

def main():
    st.title("Video Processing App")

    image_file = st.file_uploader("Upload Image File", type=["jpg", "jpeg", "png"])
    
    if image_file is not None:
        st.image(image_file, caption="Uploaded Image", use_column_width=True)


    video_file = st.file_uploader("Upload Video File", type=["mp4", "mov"])

    if video_file is not None:
        st.video(video_file)

    threshold = st.slider("Threshold Value", min_value=0.0, max_value=1.0, value=0.8, step=0.01)

    if st.button("Submit"):
        if not image_file:
            st.error("Please upload an image file.")
            return
        if not video_file:
            st.error("Please upload a video file.")
            return
        image_bytes = image_file.read()
        image_np_array = np.frombuffer(image_bytes, np.uint8)
        image_cv = cv2.imdecode(image_np_array, cv2.IMREAD_COLOR)
        filename = "some_video.mp4"

        with open(filename, "wb") as outfile:
            outfile.write(video_file.getbuffer())
            
        output_path = make_result(filename,image_cv,threshold)
        video_file = open(output_path, 'rb')
        video_bytes = video_file.read()
        st.write("Processed Video")
        st.video(video_bytes)
        os.remove(filename)

if __name__ == "__main__":
    main()