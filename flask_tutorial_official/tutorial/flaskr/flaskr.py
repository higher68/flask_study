# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
                  abort, render_template, flash
from __future__ import with statement
from contextlib import closing  # ブロックの完了時にthingをcloseするコンテキストマネージャを返す。
# 要するに、処理が完了したら閉じてくれるってことか
# コンテキストマネージャーは__enter__()と__exit__()メソッドを実行する。
# 自動でログイン・ログアウトしてくれる的な?

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


def init_db():
    '''
    データベースの初期化
    '''
    with closing(connecet_db()) as db:
        with app.open_resource('schema.sql') as f:  # なんかよくわからんが、shema.sqlを実行してるのはわかるapplication objectらしい
            db.cursor().executescript(f.read())
        db.commit()


if __name__ == "__main__":
    app.run()
            

