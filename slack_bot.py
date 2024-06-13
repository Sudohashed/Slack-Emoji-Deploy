import os
import requests

SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
CHANNEL_ID = 'YOUR_CHANNEL_ID'
SEARCH_TEXT = 'specific text'
EMOJI = 'thumbsup'

def check_messages():
    url = f"https://slack.com/api/conversations.history?channel={CHANNEL_ID}"
    headers = {"Authorization": f"Bearer {SLACK_BOT_TOKEN}"}
    response = requests.get(url, headers=headers)
    messages = response.json().get('messages', [])

    for message in messages:
        if SEARCH_TEXT in message.get('text', ''):
            timestamp = message['ts']
            react_to_message(CHANNEL_ID, timestamp, EMOJI)
            break

def react_to_message(channel, timestamp, emoji):
    url = "https://slack.com/api/reactions.add"
    headers = {"Authorization": f"Bearer {SLACK_BOT_TOKEN}"}
    payload = {
        'channel': channel,
        'name': emoji,
        'timestamp': timestamp
    }
    response = requests.post(url, headers=headers, data=payload)
    if response.json().get('ok'):
        print("Reaction added successfully.")
    else:
        print("Failed to add reaction.")

if __name__ == "__main__":
    check_messages()
