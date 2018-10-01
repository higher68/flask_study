from flask import Flask  # Flaskクラスのインポート
# WSGIアプリケーションとなるらしい。WEBサーバとアプリケーションを接続するためのインターフェースをPythonで定義したもの
# WebサーバとWebアプリの実装を切り離し、柔軟に組み合わせられる。らしい。
# https://qiita.com/habakan/items/67fb25c34a35db373c07
# add_url_ruleメソッドをdecorator()を通して実行しているらしい。
# add_url_rule()を実行して、hello()が実行される。
# アプリとして起動したときは、__name__の中身は__main__、モジュールとしてインポートされたときは、ファイル名となる
app = Flask(__name__)  # インスタンスの生成 Flaskがどこからファイルを探すかを認識するのに必要らしいが。うーん￥？
# この場合は、Flask.route()メソッドにデコレートしてる。
@app.route('/')  # デコレータ。これを使うと関数を簡単に上書きできる
def hello_world():
    return "Hello World!"

# def hello_world():
#    return "Hello World!"
# hello_world = app.route('/', hello_world())
# と同等

if __name__ == '__main__':
    app.run()  # ローカルサーバでアプリを実行
    
