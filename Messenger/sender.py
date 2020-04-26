from pprint import pprint

import requests

# он будет у нас отправлять сообщения
# нам нужно вызвать метод по отправке сообщений
print('Enter username:')
username = input()

print('Enter password:')
password = input()

while True:
    print('Enter message:')
    text = input()

    response = requests.post('http://127.0.0.1:5000/send',
                             json={"username": username, "password": password, "text": text})
    if not response.json()['ok']:
        print('Access denied')  # Доступ запрещен
        break  # Выйти из цикла чтобы завершить программу
