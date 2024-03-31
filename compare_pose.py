# Description: This file contains the code to compare the pose of two images.

import numpy as np
import cv2
import mediapipe as mp

# Initialize mediapipe pose class.
class match_pose:
    def __init__(self, image):
        self.image = image
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.8)
        self.pose_img = self.pose.process(self.image)
        self.landmark = self.pose_img.pose_landmarks
        self.skip_pose = self.check_for_face(self.image)
        self.points = np.array([(lm.x, lm.y, lm.z) for lm in self.landmark.landmark[self.skip_pose:]])

    def cosine_distance(self, landmarks2):
        if self.landmark and landmarks2:
            points1 = self.points
            points2 = np.array([(lm.x, lm.y, lm.z) for lm in landmarks2.landmark[self.skip_pose:]])
            dot_product = np.dot(points1.flatten(), points2.flatten())
            norm_product = np.linalg.norm(points1.flatten()) * np.linalg.norm(points2.flatten())
            similarity = dot_product / norm_product
            return similarity
        else:
            return 0
        
    def check_for_face(self,img):
        haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        face_cascade = cv2.CascadeClassifier(haar_file)
        faces = face_cascade.detectMultiScale(img, scaleFactor=1.3)
        if faces:
            return 0
        else:
            return 11


    def compare_images(self, im2, threshold=0.8):
        im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)
        im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)
        pose2 = self.pose.process(im2)
        landmarks2 = pose2.pose_landmarks
        similarity = self.cosine_distance(landmarks2)
        similarity = np.round(similarity, 2)
        if similarity > threshold:
            return True