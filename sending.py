import requests
from pprint import pprint
TOKEN='5559122728:AAHOu1gL4pA1riJPMCmICNTKI57P5xnHsyA'
url = 'https://cdn2.thecatapi.com/images/MTY4Njk5Ng.jpg'
file_id = 'AgACAgIAAxkBAAIBSmNRG6awCnoUmYEEEWWULqhdCV2UAALawjEbZVmJSgRD6s4szbUcAQADAgADcwADKgQ'
chat_id = 5575549228

data = {
            'chat_id':chat_id,
            'photo':file_id,
            'caption':f"<b>CAT</b>",
            'parse_mode':'HTML'
        }
    
r = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',data=data)


# def get_updates(TOKEN):
#     updates = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
#     updates = updates.json()
#     return updates


# pprint(get_updates(TOKEN))


# 'photo': [{'file_id': 'AgACAgIAAxkBAAIBSmNRG6awCnoUmYEEEWWULqhdCV2UAALawjEbZVmJSgRD6s4szbUcAQADAgADcwADKgQ',
#                                     'file_size': 1077,
#                                     'file_unique_id': 'AQAD2sIxG2VZiUp4',
#                                     'height': 66,
#                                     'width': 90},
#                                    {'file_id': 'AgACAgIAAxkBAAIBSmNRG6awCnoUmYEEEWWULqhdCV2UAALawjEbZVmJSgRD6s4szbUcAQADAgADbQADKgQ',
#                                     'file_size': 12323,
#                                     'file_unique_id': 'AQAD2sIxG2VZiUpy',
#                                     'height': 234,
#                                     'width': 320},
#                                    {'file_id': 'AgACAgIAAxkBAAIBSmNRG6awCnoUmYEEEWWULqhdCV2UAALawjEbZVmJSgRD6s4szbUcAQADAgADeAADKgQ',
#                                     'file_size': 38191,
#                                     'file_unique_id': 'AQAD2sIxG2VZiUp9',
#                                     'height': 468,
#                                     'width': 640}]},
#              'update_id': 527548165}]}
