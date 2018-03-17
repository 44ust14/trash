# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


# добавляємо секретний ключ для сайту щоб шифрувати дані сессії
# при кожнаму сапуску фласку буде генечитись новий рандомний ключ з 24 символів
app.secret_key = os.urandom(24)
# app.secret_key = '125'

@app.route('/')
def home():
    avg =
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True, port=7485)
