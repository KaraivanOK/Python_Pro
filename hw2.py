from flask import Flask, request, render_template
from faker import Faker
import csv
import requests

app = Flask(__name__)
fake = Faker()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/requrements')
def requrements():
    return open('requirements.txt', encoding='utf-16').read().splitlines()


@app.route('/generate-users')
def generate_users():
    count = request.args.get('count')
    f = [f'{fake.email()} -- {fake.name()}\n' for _ in range(int(count))]
    return f


@app.route('/mean')
def mean():
    with open('hw.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        height_inches, weight_pounds = 0, 0
        count = 0
        for row in reader:
            count += 1
            height_inches += float(row[' "Height(Inches)"'])
            weight_pounds += float(row[' "Weight(Pounds)"'])
        return f'Средний рост = {(height_inches / count) * 2.54} см' \
               f' Средний вес = {(weight_pounds / count) * 0.45359237} кг'


@app.route('/space')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    return str(r.json()["number"])


if __name__ == '__main__':
    app.run()