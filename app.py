import re
from datetime import datetime

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/projects/")
def projects():
    return render_template("projects.html")

@app.route("/practice/")
def practice():
    return render_template("practice.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = "user"):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

