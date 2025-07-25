
import json
import os
import requests

CONFIG_PATH = os.path.expanduser("~/.shipy/telegram_config.json")

def register_telegram(token: str, chat_id: str, alias: str = "default", message: str = "Registered from ShiPy 🚀"):
    try:
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "r") as f:
                config = json.load(f)
        else:
            config = {}

        config[alias] = {"token": token, "chat_id": chat_id}

        with open(CONFIG_PATH, "w") as f:
            json.dump(config, f, indent=2)

        # Send registration message
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }

        response = requests.post(url, data=payload)
        print(f"Registered '{alias}' Successfully")
        return response.json()
    
    except Exception as e:
        print(f"[x] Could not register due to {e}")


