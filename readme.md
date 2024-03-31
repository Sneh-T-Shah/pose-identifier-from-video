# Pose Estimation App

This project is aimed at detecting and comparing poses between a given image and frames in a video. It utilizes the MediaPipe library for pose estimation and Streamlit for the user interface.

## Project Structure

The project consists of the following files:

- **compare_pose.py**: This file compares the pose of a given image with poses in frames of the input video.
- **add_text_to_frame.py**: It writes the word "DETECTED" on the frames where the pose matches between the input image and video frames.
- **get_video.py**: This script plays the video and saves the resultant output video with detected poses.
- **ui_for_pose.py**: Frontend of the app built with Streamlit. Running this script initiates the user interface for interacting with the app.

## Dependencies

The project relies on the following Python libraries, which are specified in the `requirements.txt` file:

- mediapipe
- streamlit
- numpy
- python (assumed to be a system dependency)

## Usage

To run the application, follow these steps:

1. Install the dependencies by executing the following command:
    ```
    pip install -r requirements.txt
    ```

2. Run the Streamlit app by executing the following command in your terminal:
    ```
    streamlit run ui_for_pose.py
    ```

3. This will launch the user interface in your default web browser. From there, you can interact with the app by providing the input image and video.

## Additional Notes and Future Scope

- Face detection in the input image is performed using a Haar cascade classifier.
- The application currently detects and compares poses between a single input image and frames of the input video.
- Users have the option to set a threshold manually. A higher threshold means less difference between the detected pose in the frame and the actual pose.
- Future enhancements could include:
  - Extending functionality to accept video inputs for comparison, allowing users to compare poses between two videos.
  - Implementing a frame-by-frame pose estimation for video-to-video comparison.
  - Enhancing the pose estimation algorithms to handle more complex poses and scenarios.

