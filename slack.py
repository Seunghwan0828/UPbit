import requests

token = "xoxb-2455740732864-2432119597634-k0D7CyvuM4taQPxbU2txJKnk"
channel = "#alarm"
text = "hello"

requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )