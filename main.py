from cgi import test
from re import A
import requests

TOKEN='5559122728:AAHOu1gL4pA1riJPMCmICNTKI57P5xnHsyA'

new_update_length = -1

def get_updates(TOKEN):
    updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    updates = updates.json()
    return updates

def get_last_update(updates):
    last_updates = updates['result'][-1]
    chat_id = last_updates['message']['chat']['id']
    text = last_updates['message']['text']
    return chat_id,text

def send_message(TOKEN,chat_id, text):
    data = {
            'chat_id':chat_id,
            'text':text
        }
    
    r = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data=data)

while True:
    updates = get_updates(TOKEN)
    last_update = get_last_update(updates)
    chat_id, text = last_update

    last_update_length = len(updates['result'])

    if new_update_length != last_update_length:
        send_message(TOKEN,chat_id=chat_id, text=text)
        new_update_length = last_update_length
    # print("NEW UPDATE LENGTH",new_update_length, "LAST UPDATE LENGTH", last_update_length)