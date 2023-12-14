# Face Reading 

The "Face Reading" is a Python program that utilizes facial landmarks to make humorous predictions based on specific facial features. The program employs the dlib library for face detection and facial landmark extraction, providing a light-hearted and entertaining experience.

## Features:

- **Forehead Prediction:** If the user has a relatively large forehead compared to their face, the program playfully suggests, "I know you have all the answers."

- **Mouth Prediction:** A sizable mouth relative to the face prompts the program to humorously state, "Please, it's my turn to talk."

- **Cheek Prediction:** If the user's cheeks are proportionally larger, the program suggests, "You hold all the secrets."

- **Nose Prediction:** A significant nose relative to the face size triggers the question, "How many lies have you told today?"

## Instructions:

1. Ensure you have Python and the required libraries installed (`cv2`, `dlib`, `numpy`).
2. Download the facial landmarks predictor file (`shape_predictor_68_face_landmarks.dat`) and place it in the project directory.
3. Run the Python script, and the webcam feed will display with humorous predictions based on facial features.

## Setup:

1. Install dependencies:
   pip install opencv-python dlib numpy
2. Download the facial landmarks predictor file from here ->https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat
3. Extract the downloaded file and place it in the project directory.
4. Run the script:
  python facial_predictions.py
