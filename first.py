from flask import Flask
from datetime import datetime
import re
import math

app = Flask(__name__)

@app.route('/')
def home():
     return "hello my god friend"

@app.route('/hello/<name>')
def hello(name):
    now = datetime.now()
    formatted_date = now.strftime("%A, %d, %B, %Y at %X")
    match_object = re.match("[a-zA-Z]+", name)
    if match_object:
        clean_name = match_object.group(0)
    else: clean_name = "friend"
    content = "Hello there, " + clean_name + "!"+"Its now " + formatted_date
    return content

@app.route('/func')
def func():
   a = (math.gcd(12, 54))
   return str(a)
