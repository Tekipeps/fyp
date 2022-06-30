from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/lg")
def notebook():
    return render_template('lg.html')
