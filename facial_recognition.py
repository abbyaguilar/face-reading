import cv2
import dlib
import numpy as np

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX
font_size = .5
font_thickness = 1
font_color = (255, 255, 255)  # White color

window_width = 800
window_height = 500

cv2.namedWindow('Facial Predictions', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Facial Predictions', window_width, window_height)

while True:
    ret, frame = cap.read()

    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)

        # Calculate sizes relative to face width
        forehead_width = np.linalg.norm(np.array([landmarks.part(19).x, landmarks.part(24).y]) -
                                        np.array([landmarks.part(24).x, landmarks.part(24).y]))
        mouth_width = np.linalg.norm(np.array([landmarks.part(54).x, landmarks.part(54).y]) -
                                     np.array([landmarks.part(48).x, landmarks.part(48).y]))
        cheek_width = np.linalg.norm(np.array([landmarks.part(13).x, landmarks.part(13).y]) -
                                      np.array([landmarks.part(3).x, landmarks.part(3).y]))
        nose_width = np.linalg.norm(np.array([landmarks.part(35).x, landmarks.part(35).y]) -
                                     np.array([landmarks.part(31).x, landmarks.part(31).y]))

        relative_forehead_size = (forehead_width / face.width()) * 100
        relative_mouth_size = (mouth_width / face.width()) * 100
        relative_cheek_size = (cheek_width / face.width()) * 100
        relative_nose_size = (nose_width / face.width()) * 100

        forehead_prediction = "I know you have all the answers, Big Head." if relative_forehead_size > 25 else ""
        mouth_prediction = "It's my turn to do the talking, Chatterbox." if relative_mouth_size > 25 else ""
        cheek_prediction = "Do you keep secrets as a friend or enemy, Pompus Chipmunk?" if relative_cheek_size > 25 else ""
        nose_prediction = "How many lies have you told today, Pinocchio?" if relative_nose_size > 25 else ""

        y_position = 369
        for prediction in [forehead_prediction, mouth_prediction, cheek_prediction, nose_prediction]:
            if prediction:
                cv2.putText(frame, prediction, (50, y_position), font, font_size, font_color, font_thickness, cv2.LINE_AA)
                y_position += int(50 * font_size)  # Adjust the vertical spacing

    cv2.imshow('Facial Predictions', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
