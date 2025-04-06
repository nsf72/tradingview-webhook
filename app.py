from flask import Flask, request
import requests
import os

app = Flask(__name__)
LINE_NOTIFY_TOKEN = os.getenv("LINE_NOTIFY_TOKEN")

def send_line_notify(message):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'}
    data = {'message': message}
    return requests.post(url, headers=headers, data=data)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    symbol = data.get("symbol", "Unknown")
    event = data.get("event", "No event")
    time = data.get("time", "N/A")

    message = f"🚨 {symbol} 發生訊號\n🕒 {time}\n📢 {event}"
    send_line_notify(message)

    return {"status": "ok"}
