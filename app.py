from flask import Flask, render_template, request, flash, redirect, url_for
from hashids import Hashids
import requests
import os
import base64

app = Flask(__name__)

app.config['SECRET_KEY'] = 'this should be a secret random string'

hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/API')
def API():
    return render_template('API.html')

@app.route('/encode', methods=['POST'])
def encode():
    if request.method == 'POST':
        message = request.form['user_url']
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return render_template('index.html',msg = base64_message)

@app.route('/encode/', methods=['GET'])
def user_encode():
    message = request.args.get('code')
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    base64_message = "Encoded Message: " + base64_message
    return render_template('out.html',msg = base64_message)

@app.route('/decode/', methods=['GET'])
def user_decode():
    base64_message = request.args.get('code')
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    message = "Decoded Message : " + message
    return render_template('out.html',msg2 = message)

@app.route('/decode', methods=['POST'])
def decode():
    if request.method == 'POST':
        base64_message = request.form['user_url']
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        return render_template('index.html',msg2 = message)
    
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
