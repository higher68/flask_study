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
# ルーティング：URLと処理を対応づけること。urlとfunctionをflaskでは結びつける。route()で行う


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


@app.route('/')  # http://xxx 以降のURLパスを '/' と指定
def show_entries():
    '''
    return show_entries.htmlを読み込む際に、entriesという変数を渡す。
    '''
    cur = g.db.execute('select title, text from entriew order by id desc')
    # execute()はsql文の実行
    # title:row[0], text:row[1]
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    # feetchallは全ての(残りの)クエリ結果の row をフェッチして、リストを返す
    return render_template('show_entries.html', entries=entries)

# ハンドルは処理を行うってこと？
# おそらく、下のデコレータは、特定のhttpメソッドの時だけハンドルしてる?
# route()は、HTTPメソッド名を渡すと、URLが受け入れるHTTPメソッドを指定できる
# HTTPメソッドは、クライアントが行いたい処理をサーバに伝える種類は、色々あるよ
# postはリソースへのデータ追加とかする。
@app.route('/add', methods=['POST'])
def add_entry():
    '''
    ログイン時に新規エントリーを追加するview
    
    '''
    # session：一度ログインしたら、それ以降はどのページでもログインした状態にできるようにする
    # 下だと、ログインキーを取得してる
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries')



if __name__ == "__main__":
    app.run()
            

