from flask import Flask, request
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discordapp.com/api/webhooks/1358346547061981284/dsR-W1YAc7ucrpkXA5RjuTj622CcJbVAeHLEKX-wcXOnGevgvHk5xQEecVCSnZ7x7RCn"

def send_discord_message(message):
    data = {
        "content": message
    }
    return requests.post(DISCORD_WEBHOOK_URL, json=data)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    symbol = data.get("symbol", "Unknown")
    event = data.get("event", "No event")
    time = data.get("time", "N/A")

    message = f"\ud83d\udea8 {symbol} \u767c\u751f\u8a0a\u865f\n\ud83d\udd52 {time}\n\ud83d\udce2 {event}"
    send_discord_message(message)

    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

