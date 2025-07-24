import requests
import os
import dotenv

dotenv.load_dotenv()
token = os.getenv("TELEGRAM_TOKEN")

class Telegram:
    def __init__(self, bot_token: str):
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{bot_token}"

    def sail(self, chat_id: str, message: str, all : bool = False) -> dict:
        url = f"{self.base_url}/sendMessage"
        payload = {
            "chat_id": chat_id,
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
            return result
        else:
            print(to_print)
            return to_print
