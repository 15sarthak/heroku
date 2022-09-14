from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<number>")
def second(number):
    return f"<p>Hello, World! -- {number}</p>"


if __name__ == '__main__':
    app.run(debug=True)