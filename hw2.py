from flask import Flask, request, render_template
from faker import Faker
import csv
import requests

app = Flask(__name__)
fake = Faker()


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/requrements')
def requrements():
    f = open('requirements.txt', encoding='utf-16').read().splitlines()
    return render_template('requrements.html', f=f)


@app.route('/generate-users')
def generate_users():
    count = request.args.get('count')
    if count is None:
        count = 100
    f = [f'{fake.email()} -- {fake.name()}\n' for _ in range(int(count))]
    return render_template('generate-users.html', f=f)


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
        height_sm = f'Средний рост = {(height_inches / count) * 2.54} см'
        weight_kg = f' Средний вес = {(weight_pounds / count) * 0.45359237} кг'
        f = [height_sm, weight_kg]
        return render_template('mean.html', f=f)


@app.route('/space')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    return str(r.json()["number"])


if __name__ == '__main__':
    app.run(debug=True)
