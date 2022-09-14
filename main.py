from flask import Flask,request
from firebase_admin import credentials,initialize_app
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<number>")
def second(number):
    return f"<p>Hello, World! -- {number}</p>"


if __name__ == '__main__':
    app.run(debug=True)