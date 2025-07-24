# ShiPy - Write once send anywhere!

A pip installable that allows to send messages from python to any platform, like telegram, slack etc. Built for plug and play!
No need to worry about platform-specific APIs or boilerplate code. Just install, register, and sail your messages 

> Note: `ShiPy` is actively under development. This is a refence documentation.
> v0 will soon be published to PyPI

## Purpose
ShiPy simplifies how your Python scripts talk to the outside world.

Whether it's a success message after deployment, a failure alert, or just a friendly "Job Done!" ping — ShiPy lets you send updates from your code directly to platforms like Telegram (and more soon!) with just one line.

No complex APIs. No boilerplate.
Just plug it in and sail your messages effortlessly. ⛵

## How ShiPy feels: 

1. Install ShiPy.
```
pip install ShiPy
```

2. If you are a first time user, register yourself.
```
register("telegram", token=telegram_token, chat_id=chat_id, alias = "Yadh")
```

3. Create an object.
```
ship = Telegram("Yadh")
```

4. Sail your ship!
```
ship.sail("Message from ShiPy")
```

---

## Author

#### Yadhnika Wakde - Backend Developer
> Hope ShiPy helps!





