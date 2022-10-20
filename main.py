import requests

TOKEN='5559122728:AAHOu1gL4pA1riJPMCmICNTKI57P5xnHsyA'

def get_updates(TOKEN):
    updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    updates = updates.json()
    return updates

def get_last_update(updates):
    last_updates = updates['result'][-1]
    chat_id = last_updates['message']['chat']['id']
    text = last_updates['message']['text']
    message_id = last_updates['message']['message_id']
    return chat_id, text, message_id

def send_message(TOKEN,chat_id, text):
    data = {
            'chat_id':chat_id,
            'text':f"_*{text}*_",
            'parse_mode':'MarkdownV2'
        }
    
    r = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data=data)

new_message_id = -1

while True:
    updates = get_updates(TOKEN)
    last_update = get_last_update(updates)
    chat_id, text, last_message_id = last_update

    if new_message_id != last_message_id:
        send_message(TOKEN,chat_id=chat_id, text=text)
        new_message_id = last_message_id
    print("NEW MESSAGE ID",new_message_id, "LAST MESSAGE ID", last_message_id)