from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'It\'s alive!'
  
@app.route('/hello')
def say_hello():
  return 'Hello cruel world do you know that you\'re killing me?'
