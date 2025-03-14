# 03-137: Flask Environment setup

## app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World Flask'

if __name__ == '__main__':
    app.run(debug=True)