import text

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return text.random_python_quote()
