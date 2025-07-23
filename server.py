from flask import Flask, request, redirect
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return "Server is Running"

@app.route('/upload', methods=['POST'])
def upload():
    if 'photo' not in request.files:
        return "No photo uploaded", 400

    photo = request.files['photo']
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{UPLOAD_FOLDER}/image_{timestamp}.jpg"
    photo.save(filename)

    return "Uploaded"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
