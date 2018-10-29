from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/answer')
def answer():
    return render_template('answer.html')
