from flask import Flask
from flask import render_template  # 特定のルーティングからテンプレエンジンを呼び出す
from flask import request  # ユーザから要求されるリクエストを受け取るライブラリート
# Flaskクラスのインポート
app = Flask(__name__)  # アプリの本体をインスタンスとして作成
# webアプリでは、http://のあとの最初の/で、ユーザーのリクエストの種類を見分けている。
# ルーティング＝サーバ側にこの処理の振り分けを実装する
# flaskでは@app.route()のデコレータをルーティングを表す関数の直前に配置
# それによってルーティングのルールを決定
# defaultでは、Flaskのアプリはlocalhost:5000でリクエストを待ってる
# @app.route('/')なら、localhost:5000にアクセスした時のレスポンス
# @app.route('/hoge')なら、localhost:5000/hogeにアクセスした時のレスポンスを指定
app = Flask(__name__)

# 下記、routing部分の<title>は、x:/title/<title>へのアクセス、o:<title>の位置に入力された文字列をルーティング関数内で使えるようにする処理。要するに、title=input()ってこと？
# <title>で受け取った値はtitle関数の中で同じ名前の引数として渡される。
@app.route('/title/<title>')
def title(title):
    return render_template('index.html', title=title)

# ルーティングからユーザがパスに入力した値を利用する例
@app.route('/user/<string:username>')  # stringに引数の型を指定
def user(username):
    return username


@app.route('/user/<int:user_id>')
def user_id(id):
    return id


@app.route('/search')
def search():
    '''
qで指定されたパラメータを取得
URLのパラメータを取得
'''
    q = request.args.get('q', '')
    return q  # ?q=何ちゃらの何ちゃらが出力される。returnなのに注意。htmlは介してない。

@app.route('/login', methods=['GET'])
def render_form():
    return render_template('login.html')

# request.formってもしや、formタグの変数を指定すると受け取れるってことかな
@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['email']:
        return render_template('check.html', email=request.form['email'], username=request.form['username'])
    else:
        return render_template('error.html')
    

# /にアクセスがあった時の処理
@app.route('/')
def hello_world():
    return """
<!DOCTYPE>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet"
href="/static/style.css"/>
</head>
<body>
<h1> Hello World</h1>
</body>
</html>
"""


@app.route('/hoge', methods=['GET'])
def hoge():
    return 'hoge'
@app.route('/hoge', methods=['POST'])
def Hoge():
    return "Hoge"

@app.route('/foo/')
def foo():
    return 'foo'  # この場合foo/としなくてもURLに飛べる


@app.route('/fuga')
def fuga():
    return 'fuga'  # この場合fuga/とすると飛べない


