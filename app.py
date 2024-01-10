from flask import Flask, render_template, redirect, url_for
import cv2
import face_recognition
import numpy as np

app = Flask(__name__)

# Load known faces
known_image_paths = ["Faces/Anushka_0.jpg", "Faces/Satyam_25.jpg"]
known_names = ["Anushka", "Satyam"]
known_encodings = [face_recognition.face_encodings(face_recognition.load_image_file(img_path))[0] for img_path in known_image_paths]

def recognize_person(face_encoding):
    matches = face_recognition.compare_faces(known_encodings, face_encoding)
    name = "Unknown"
    if True in matches:
        name = known_names[matches.index(True)]
    return name

def process_video():
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    name = "Unknown"
    for face_encoding in face_encodings:
        name = recognize_person(face_encoding)
    video_capture.release()
    cv2.destroyAllWindows()
    return name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    name = process_video()
    if name == "Satyam":
        return redirect(url_for('happy'))
    return render_template('index.html', error="Face not recognized. Please try again.")

@app.route('/happy')
def happy():
    return render_template('happyPage.html')

if __name__ == '__main__':
    app.run(debug=True)
