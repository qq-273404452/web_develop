from flask import Flask, render_template
from pymongo import MongoClient
from threading import Lock
from flask_socketio import SocketIO


async_mode = None

app=Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)

thread = None
thread_lock = Lock()

db=MongoClient()
col=db['testdb']['users']

def background_thread():
    count = 0

    for x in col.find({}, {'_id': 0, 'time': 1, 'value': 1}):
        socketio.sleep(5)
        count+=1
        t= x['time']
        cpus = x['value']
        socketio.emit('server_response',
                      {'data': [t, *cpus], 'count': count},
                      namespace='/test')  # 注意：这里不需要客户端连接的上下文，默认 broadcast = True ！！！！！！！


'''

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(5)
        count += 1
        t = time.strftime('%M:%S', time.localtime()) # 获取系统时间（只取分:秒）
        cpus = psutil.cpu_percent(interval=None, percpu=True) # 获取系统cpu使用率 non-blocking
        socketio.emit('server_response',
                      {'data': [t, *cpus], 'count': count},
                      namespace='/test') # 注意：这里不需要客户端连接的上下文，默认 broadcast = True ！！！！！！！

'''
@app.route('/')
def index():
    return render_template('line.html')

# 与前端建立 socket 连接后，启动后台线程
@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='5000',debug= True)