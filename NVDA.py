import requests
import json

def fetch_stocktwits_messages():
    url = "https://api.stocktwits.com/api/2/streams/symbol/NVDA.json?"
    response = requests.get(url)
    data = response.json()

    messages = data.get("messages", [])
    for message in messages:
        print(message['body'])

# Call the function
fetch_stocktwits_messages()