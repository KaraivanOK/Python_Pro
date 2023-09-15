from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def conn():
    with sqlite3.connect('HW3') as db:
        cur = db.cursor()
        return cur


@app.route('/')
def home():
    return 'HW3'


@app.route('/names/')
def names():
    connect = conn()
    distinct_names = connect.execute(
        """SELECT DISTINCT first_name FROM сustomers""").fetchall()
    return render_template('names.html', distinct_names=distinct_names)


@app.route('/customers/')
def customers():
    id_customer = request.args.get('id')
    first_name = request.args.get('first_name')
    desc = request.args.get('desc')
    last_name = request.args.get('last_name')
    connect = conn()
    customers_table = connect.execute(
        """SELECT * FROM сustomers""").fetchall()
    if id_customer is None and first_name is None and last_name is None \
            and desc is None:
        return render_template('customers.html',
                               customers_table=customers_table)
    if id_customer is not None:
        customers_table = [customers_table[int(id_customer) - 1]]
        return render_template('customers.html',
                               customers_table=customers_table)
    if first_name is not None:
        customers_table_first_name_search = []
        for item in customers_table:
            if item[1] == first_name:
                customers_table_first_name_search.append(item)
        return render_template('customers.html',
                               customers_table=customers_table_first_name_search
                               )
    if last_name is not None:
        customers_table_last_name_search = []
        for item in customers_table:
            if item[2] == last_name:
                customers_table_last_name_search.append(item)
        return render_template('customers.html',
                               customers_table=customers_table_last_name_search)
    if desc is not None:
        customers_table = connect.execute(
            """SELECT * FROM сustomers ORDER BY id DESC""").fetchall()
        return render_template('customers.html',
                               customers_table=customers_table)


@app.route('/tracks/count')
def tracks_count():
    connect = conn()
    count = connect.execute(
        """SELECT COUNT(*) FROM tracks""").fetchall()
    return render_template('tracks_count.html', count=count)


@app.route('/tracks/duration')
def tracks_duration():
    connect = conn()
    tracks_all = connect.execute(
        """SELECT name,duration FROM tracks""").fetchall()
    return render_template('tracks_duration.html', tracks_all=tracks_all)


if __name__ == '__main__':
    app.run(debug=True)
