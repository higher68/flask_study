# all the imports
import sqlite3
from flask import Flask, request, session, g, redikrect, url_for, \
    abort, render_templeate, flash

# configuration
DATABASE = '/tmp/flask.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application
app = Flask(__name__)
app.config.from_object(__name__)  # 与えられたオブジェクト内の大文字の変数全て取得

def connect_db():
    '''
    データベースにコネクトするメソッド
    '''
    return sqlite3.connect(app.config["DATABASE"])

if __name__ === "__main__":
    app.run()  # ファイルが直接実行された時に限りスタンドアロンでflaskrが起動

