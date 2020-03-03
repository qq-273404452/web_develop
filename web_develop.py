# coding=utf-8
from flask import Flask, request, render_template
from flask.views import View

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')