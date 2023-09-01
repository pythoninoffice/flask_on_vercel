from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Vercel!</p>"

@app.route("/yoyo")
def yoyo():
    return render_template("yoyo.html")
