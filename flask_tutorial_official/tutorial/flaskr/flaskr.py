# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
                  abort, render_template, flash

# configuration
DATABASE = "/tmp/flaskr.db"
DEBUG = True
SECRET_KEY = "development key"
USERNAME = "admin"
PASSWORD = "default"

# create our little application
app = Flask(__name__)
app.config.from_object(__name__)  # 与えたオブジェクト内部で大文字の変数を全て取得。外からも渡せる。
# 環境変数から設定を引き継ぐ場合
# app.config.from_envvar("FLASK_SETTINGS", silent=True)


def connect_db():
    '''データベースにコネクトする。思想的には、アクセスするというよりも、コネクションを作るらしい。
    今回の引数はデータベース名
    
    return connectionオブジェクト。データベースを表すらしい
    '''
    return sqlite3.connect(app.config["DATABASE"])


if __name__ == "__main__":
    app.run()
            

