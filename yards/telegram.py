from shipy.register.reg_telegram import CONFIG_PATH
import requests
import os
import dotenv
import json

dotenv.load_dotenv()

# token = os.getenv("TELEGRAM_TOKEN")

class Telegram:
    def __init__(self, chat_id : str, bot_token: str):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{bot_token}"

    def sail(self, message: str, all : bool = False) -> dict:
        url = f"{self.base_url}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": message
        }
        response = requests.post(url, data=payload)
        result = response.json()

        to_print = {
            "ok": result.get("ok"),
            "text": result.get("result", {}).get("text")  
}   
        if all:
            print(result)
            # return result
        else:
            print(to_print)
            # return to_print

    def _load_config(self):
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "r") as f:
                return json.load(f)
        raise Exception("Telegram config not found. Please register first.")
