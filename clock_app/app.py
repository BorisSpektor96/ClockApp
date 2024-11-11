from flask import Flask, jsonify, request
from datetime import datetime, timedelta

app = Flask(__name__)
current_time = datetime.now()

@app.route('/')
def index():
    return f"Current time: {current_time.strftime('%H:%M:%S')}"

@app.route('/update_time', methods=['POST'])
def update_time():
    global current_time
    seconds_decrement = int(request.form['seconds'])
    current_time -= timedelta(seconds=seconds_decrement)
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

