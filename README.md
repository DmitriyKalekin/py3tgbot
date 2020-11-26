# py3tgbot
Simple async python 3 telegram bot using fast aiohttp requests

View at:
https://test.pypi.org/project/py3tgbot

## How to install
```bash
pip3 install py3tgbot  
```

## Usage
```python
import asyncio
from py3tgbot import TgBotJson


TGBOT_TOKEN = "12345:YOUR_TOKEN"
APP_HOSTNAME = "https://YOUR_HOSTNAME.ngrok.io"
CHAT_ID = 123456789  # your chat id

client_tgbot = TgBotJson(token=TGBOT_TOKEN)


async def main_async():
    response = await app.client_tgbot.setWebhook("{hostname}/tgbot/wh".format(hostname=APP_HOSTNAME))
    r = await response.json()
    print(r)

    response = await app.client_tgbot.sendMessage(CHAT_ID, "Hello from Telegram Bot!")
    r = await response.json()
    print(r)


if __name__ == "__main__":
    asyncio.run_until_complete(main_async())

```



### Docs
1. How to publish pypi package [Medium article in Russian](https://medium.com/nuances-of-programming/python-%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F-%D0%B2%D0%B0%D1%88%D0%B8%D1%85-%D0%BF%D0%B0%D0%BA%D0%B5%D1%82%D0%BE%D0%B2-%D0%B2-pypi-11dd3216581c)








