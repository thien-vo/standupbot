from flask import Flask, render_template
import logging


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run('0.0.0.0')