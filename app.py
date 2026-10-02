import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def conatct():
    return render_template('contact.html')

@app.route('/news')
def backup():
    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)
