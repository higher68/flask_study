# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
                  abort, render_template, flash
from __future__ import with statement
from contextlib import closing  # ブロックの完了時にthingをcloseするコンテキストマネージャを返す。
# 要するに、処理が完了したら閉じてくれるってことか
# コンテキストマネージャーは__enter__()と__exit__()メソッドを実行する。
# 自動でログイン・ログアウトしてくれる的な?
# gはグローバル変数を用意してくれるライブラリだそうで。

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
            # .cursorはcursorインスタンスを生成
            # .executescript(sql_script)はSQL文を実行する
            # cursorは表の中の1行を特定する道具。特定したあとで処理を行う
        db.commit() # 現在のトランザクションをコミット。これをすると変更が反映される。
        # コミット：トランザクション処理を確定すること
        # 分割できない一連の処理の単位


@app.before_request
def before_request():
    '''今のデータベースとのコネクションが保存
    '''
    g.db = connect_db()



@app.after_request
def after_request(response):
    '''gで保存されたコネクションをクローズ。DBからのレスポンスをクライアントに渡す。
    '''
    g.db.close()
    return response
    

if __name__ == "__main__":
    app.run()
            

