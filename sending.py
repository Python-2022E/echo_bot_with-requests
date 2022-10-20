import requests

TOKEN='5559122728:AAHOu1gL4pA1riJPMCmICNTKI57P5xnHsyA'
url = 'https://cdn2.thecatapi.com/images/MTY4Njk5Ng.jpg'
chat_id = 5575549228

data = {
            'chat_id':chat_id,
            'photo':url,
            'caption':f"<b>CAT</b>",
            'parse_mode':'HTML'
        }
    
r = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',data=data)

print(r.status_code)
