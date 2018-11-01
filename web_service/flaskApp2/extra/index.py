from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/flasknote"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # localでpostgresqlを動かす用
db = SQLAlchemy(app)  # アプリのインスタンスをセット


@app.route('/')
def hello_world():
    return "Hello world"
