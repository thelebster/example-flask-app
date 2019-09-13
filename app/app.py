from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'Online!'
  
@app.route('/greet')
def say_hello():
  return 'Hello, World!'
