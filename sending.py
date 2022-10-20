import requests

TOKEN='5559122728:AAHOu1gL4pA1riJPMCmICNTKI57P5xnHsyA'
url = 'https://krasivosti.pro/uploads/posts/2021-04/1618326499_50-p-malenkaya-martishka-obezyani-krasivo-foto-57.jpg'
chat_id = 5575549228

data = {
            'chat_id':chat_id,
            'photo':url
        }
    
r = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto',data=data)

print(r.status_code)
