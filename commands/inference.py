import os
from keras.models import load_model
import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import math
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", type=str, required=True,
                help="path to saved .keras model, eg: dir/model.keras")
ap.add_argument("-c", "--conf", type=float, required=True,
                help="min prediction conf to detect pose class (0<conf<1)")
ap.add_argument("-i", "--source", type=str, default="0",
                help="path to sample image or video source, or webcam index (default: 0)")
ap.add_argument("--save", action='store_true',
                help="Save video")

args = vars(ap.parse_args())
source = args["source"]
path_saved_model = args["model"]
threshold = args["conf"]
save = args['save']

##############
# Update class names
class_names = [
    'Chair', 'Cobra', 'Dog',
    'Tree', 'Warrior'
]
##############

torso_size_multiplier = 2.5
n_landmarks = 33
n_dimensions = 3
landmark_names = [
    'nose',
    'left_eye_inner', 'left_eye', 'left_eye_outer',
    'right_eye_inner', 'right_eye', 'right_eye_outer',
    'left_ear', 'right_ear',
    'mouth_left', 'mouth_right',
    'left_shoulder', 'right_shoulder',
    'left_elbow', 'right_elbow',
    'left_wrist', 'right_wrist',
    'left_pinky_1', 'right_pinky_1',
    'left_index_1', 'right_index_1',
    'left_thumb_2', 'right_thumb_2',
    'left_hip', 'right_hip',
    'left_knee', 'right_knee',
    'left_ankle', 'right_ankle',
    'left_heel', 'right_heel',
    'left_foot_index', 'right_foot_index',
]

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

col_names = []
for i in range(n_landmarks):
    name = mp_pose.PoseLandmark(i).name
    name_x = name + '_X'
    name_y = name + '_Y'
    name_z = name + '_Z'
    name_v = name + '_V'
    col_names.append(name_x)
    col_names.append(name_y)
    col_names.append(name_z)
    col_names.append(name_v)

# Load saved model
model = load_model(path_saved_model)

# Check if source is webcam
if source.isdigit():
    source = int(source)

# Video processing (works for both webcam and video file)
cap = cv2.VideoCapture(source)
source_width = int(cap.get(3))
source_height = int(cap.get(4))

# Write Video
if save:
    out_video = cv2.VideoWriter('output.avi', 
                        cv2.VideoWriter_fourcc(*'MJPG'),
                        10, (source_width, source_height))

while True:
    success, img = cap.read()
    if not success:
        print('[ERROR] Failed to Read Video feed')
        break
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = pose.process(img_rgb)

    if result.pose_landmarks:
        lm_list = []
        for landmarks in result.pose_landmarks.landmark:
            # Preprocessing
            max_distance = 0
            lm_list.append(landmarks)
        center_x = (lm_list[landmark_names.index('right_hip')].x +
                    lm_list[landmark_names.index('left_hip')].x)*0.5
        center_y = (lm_list[landmark_names.index('right_hip')].y +
                    lm_list[landmark_names.index('left_hip')].y)*0.5

        shoulders_x = (lm_list[landmark_names.index('right_shoulder')].x +
                       lm_list[landmark_names.index('left_shoulder')].x)*0.5
        shoulders_y = (lm_list[landmark_names.index('right_shoulder')].y +
                       lm_list[landmark_names.index('left_shoulder')].y)*0.5

        for lm in lm_list:
            distance = math.sqrt((lm.x - center_x) **
                                 2 + (lm.y - center_y)**2)
            if(distance > max_distance):
                max_distance = distance
        torso_size = math.sqrt((shoulders_x - center_x) **
                               2 + (shoulders_y - center_y)**2)
        max_distance = max(torso_size*torso_size_multiplier, max_distance)

        pre_lm = list(np.array([[(landmark.x-center_x)/max_distance, (landmark.y-center_y)/max_distance,
                                 landmark.z/max_distance, landmark.visibility] for landmark in lm_list]).flatten())
        data = pd.DataFrame([pre_lm], columns=col_names)
        predict = model.predict(data)[0]
        if max(predict) > threshold:
            pose_class = class_names[predict.argmax()]
            print('predictions: ', predict)
            print('predicted Pose Class: ', pose_class)
        else:
            pose_class = 'Unknown Pose'
            print('[INFO] Prediction is below given Confidence!!')

        # Show Result
        img = cv2.putText(
            img, f'{pose_class}',
            (40, 50), cv2.FONT_HERSHEY_PLAIN,
            2, (255, 0, 255), 2
        )
    # Write Video
    if save:
        out_video.write(img)

    cv2.imshow('Output Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
if save:
    out_video.release()
    print("[INFO] Out video Saved as 'output.avi'")
cv2.destroyAllWindows()
print('[INFO] Inference on Videostream is Ended...')
