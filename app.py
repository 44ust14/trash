# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for, session
import os
from math import ceil

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


# добавляємо секретний ключ для сайту щоб шифрувати дані сессії
# при кожнаму сапуску фласку буде генечитись новий рандомний ключ з 24 символів
app.secret_key = os.urandom(24)
# app.secret_key = '125'

@app.route('/')
def home():
    context = {}
    sum_c_min =
    pre_avg_c_min =
    avg_c_min = ceil(pre_avg_c_min)
    context['c_min'] = avg_c_min
    sum_c_max =
    pre_avg_c_max =
    avg_c_max = ceil(pre_avg_c_max)
    context['c_max'] = avg_c_max
    sum_c_current =
    pre_avg_c_current =
    avg_c_current = ceil(pre_avg_c_current)
    context['c_current'] =
    # видумати логіку вираховування статусу емодзі на основі середньої темпаратури ,опадів,приготувати емодзі
    context['status'] = 5
    sum_wind =
    pre_avg_wind =
    avg_wind = ceil(pre_avg_wind)
    context['wind'] =6
    context['c_feel'] ='загуглити як на основі погодних даних виводити :як відчувається'
    sum_precipitation =
    pre_avg_precipitation =
    avg_precipitation = ceil(pre_avg_precipitation)
    context['precipitation'] =8
    return render_template('home.html',context=context)
if __name__ == '__main__':
    app.run(debug=True, port=7778)
