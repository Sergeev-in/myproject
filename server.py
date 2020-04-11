import time
from datetime import datetime

from flask import Flask

app = Flask(__name__)  # создаем приложение


@app.route("/")  # главный локатор
def hello():  # вызываем функцию и возвращаем ее
    return "Hello, World!"


@app.route("/status")  # обрабатывает функцию status как адрес(ссылку) на функцию представления нашего приложения.
def status():  # вызываем функцию и возвращаем ее
    return {'Status': True,
            'time': datetime.now()}
    # либо можем использовать 'time': time.ctime()} #получаем актуальное время на сервере.
    # если использовать просто time, то время будет показываться в виде - float (секунды).
    # также можно использовать strftime ('') - для вольного написания формата времени и даты.


app.run()  # запуск

# То есть чтобы при запуске нашего приложения увидеть "Hello, World!", нам нужно обратится к функции hello,
# которая вернет нам эту строку, А функция вызывается с помощью указания ее имени как пути к странице приложения.