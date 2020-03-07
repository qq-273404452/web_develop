from flask import Flask, Blueprint, render_template
from pymongo import MongoClient
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Never tell you!'
socketio = SocketIO(app)

bp=Blueprint('user', __name__, url_prefix='/user')

@app.route('/')
def index():
    return render_template('base.html')

@socketio.on('message')
def handle_message(message):
    print('received message:' + message)

def get_data():
    client = MongoClient('localhost', 27017)
    db = client.testdb
    col = db.user()
    data=col.find_

if __name__ == '__main__':
    socketio.run(app,host='127.0.0.1',port='8080',debug=True)
