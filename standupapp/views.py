from flask import render_template
from standupapp import app

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/test')
def test():
    return render_template("record.html")