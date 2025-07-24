
import json
import os
import requests

CONFIG_PATH = os.path.expanduser("~/.shipy/telegram_config.json")

def register_telegram(token: str, chat_id: str, message: str = "Registered from ShiPy 🚀"):
    try:
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        with open(CONFIG_PATH, "w") as f:
            json.dump({"token": token, "chat_id": chat_id}, f)

        # Send registration message
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }

        response = requests.post(url, data=payload)
        print("Registered Successfully")
        return response.json()
    
    except Exception as e:
        print(f"Could not register due to {e}")



