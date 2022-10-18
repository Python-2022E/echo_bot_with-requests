from cgi import test
import requests

TOKEN='5559122728:AAHOu1gL4pA1riJPMCmICNTKI57P5xnHsyA'

new_update_length = -1
while True:
    updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')

    updates = updates.json()
    last_updates = updates['result'][-1]

    chat_id = last_updates['message']['chat']['id']
    text = last_updates['message']['text']
    last_update_length = len(updates['result'])

    if new_update_length != last_update_length:
        data = {
            'chat_id':chat_id,
            'text':text
        }
    
        r = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data=data)
        new_update_length = last_update_length
    print("NEW UPDATE LENGTH",new_update_length, "LAST UPDATE LENGTH", last_update_length)






















# def get_updates(TOKEN):
#     r = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
#     updates = r.json()
#     return updates

# def send_message(chat_id, text):
#     data = {
#         'chat_id':chat_id,
#         'text':text
#     }
#     requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage',data=data)

# def get_last_updates(updates):

#     last_updates = updates['result'][-1]

#     chat_id = last_updates['message']['chat']['id']
#     text = last_updates['message']['text']
#     return chat_id, text

# new_msg_len = 1
# while True:
#     data = get_updates(TOKEN)

#     last_msg_len = len(data['result'])
    
#     chat_id,text = get_last_updates(data)
#     if last_msg_len != new_msg_len:
#         send_message(chat_id,text)

#         new_msg_len = last_msg_len