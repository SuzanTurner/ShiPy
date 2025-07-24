

def register_telegram(token: str, chat_id: str, message: str = "Registered from ShiPy 🚀"):
    import requests

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(url, data=payload)
    return response.json()
