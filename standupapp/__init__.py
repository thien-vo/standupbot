from flask import Flask, render_template
import logging

app = Flask(__name__, static_url_path='/static')


import standupapp.views


if __name__ == '__main__':
    app.run('0.0.0.0')