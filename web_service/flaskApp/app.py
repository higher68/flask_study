from flask import Flask
# Flaskクラスのインポート
app = Flask(__name__)  # アプリの本体をインスタンスとして作成
# webアプリでは、http://のあとの最初の/で、ユーザーのリクエストの種類を見分けている。
# ルーティング＝サーバ側にこの処理の振り分けを実装する
# flaskでは@app.route()のデコレータをルーティングを表す関数の直前に配置
# それによってルーティングのルールを決定
# defaultでは、Flaskのアプリはlocalhost:5000でリクエストを待ってる
# @app.route('/')なら、localhost:5000にアクセスした時のレスポンス
# @app.route('/hoge')なら、localhost:5000/hogeにアクセスした時のレスポンスを指定


# /にアクセスがあった時の処理
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hoge')
def hoge():
    return 'hoge!'
