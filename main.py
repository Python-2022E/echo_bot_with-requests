from cgi import test
import requests

TOKEN='5559122728:AAHOu1gL4pA1riJPMCmICNTKI57P5xnHsyA'

def get_updates(TOKEN):
    r = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    updates = r.json()
    return updates

def send_message(chat_id, text):
    data = {
        'chat_id':chat_id,
        'text':text
    }
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data=data)

def get_last_updates(updates):

    last_updates = updates['result'][-1]

    chat_id = last_updates['message']['chat']['id']
    text = last_updates['message']['text']
    return chat_id, text

