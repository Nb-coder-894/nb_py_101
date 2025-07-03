from flask import Flask

app = Flask(__name__)

@app.route("/h")
def home():
    return "<p>home</p>"

@app.route("/work")
def hello_world():
    return "<p>hello sir</p>"