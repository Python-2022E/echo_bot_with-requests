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
    r = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data=data)
    print(r.status_code)

chat_id = 5575549228
send_message(chat_id,'Hi')