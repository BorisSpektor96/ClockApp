from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)
clock_app_url = os.getenv('CLOCK_APP_URL', 'http://clock_app:5001/update_time')

@app.route('/')
def index():
    return render_template('button.html')

@app.route('/decrement_time', methods=['POST'])
def decrement_time():
    seconds = int(request.form['seconds'])
    response = requests.post(clock_app_url, data={'seconds': seconds})

    if response.status_code == 200:
        return 'Time decremented successfully'
    else:
        return 'Failed to decrement time'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
