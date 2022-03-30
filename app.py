# from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect
from random import choice  # noqa: E402
import string  # noqa: E402
import sqlite3

app = Flask(__name__)  # noqa: E402
# db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# class Url(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     fullUrl = db.Column(db.String, unique=True)
#     shortUrl = db.Column(db.String(30), unique=True)

urls = {"abc", "cde"}  # noqa: E402


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def generate_short_id(num_of_chars: int):
    # """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/corto', methods=['GET', 'POST'])
def create_corto():
    if request.method == 'POST':
        corto_id = generate_short_id(8)
        full_url = request.form.get("full-url")

        conn = get_db_connection()
        conn = get_db_connection()
        conn.execute('INSERT INTO urls (full_url, short_url) VALUES (?, ?)',
                     (full_url, corto_id))
        conn.commit()
        conn.close()
        # print(request.form)
        # piece_count = request.form['piece_count']
        # result = pricer.predict(piece_count)
        return render_template('home.html', title='Result')
    else:
        pass
        # return render_template('predict.html', default=0, result=0, title='Predict')


@app.route('/corto/<string_id>', methods=['GET', 'POST'])
def corto_url(string_id):
    if request.method == 'GET':
        if string_id in urls:
            return redirect("http://www.example.com", code=302)
        else:
            return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
