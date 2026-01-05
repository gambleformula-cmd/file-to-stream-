import requests
from config import BOT_TOKEN, CHANNEL_USERNAME

def check_join(user_id):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMember"
    data = {
        "chat_id": CHANNEL_USERNAME,
        "user_id": user_id
    }
    r = requests.post(url, data=data).json()
    if "result" in r:
        return r["result"]["status"] in ["member", "administrator", "creator"]
    return False
