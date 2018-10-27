from flask import Flask
from flask import render_template  # 特定のルーティングからテンプレエンジンを呼び出す
from flask import request  # ユーザから要求されるリクエストを受け取るライブラリート
# Flaskクラスのインポート
from werkzeug.utils import secure_filename  # アップロードされたファイル名から自動的に安全なファイル名を作成して保存するよう設定できる
from random import random
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

# ルーティングからユーザがパスに## 入力した値を利用する例
## @app.route('/user/<string:username>')  # stringに引数の型を指定
## def user(username):
##     return username


## @app.route('/user/<int:user_id>')
## def user_id(id):
##     return id


## @app.route('/search')
## def search():
##     '''
## qで指定されたパラメータを取得
## URLのパラメータを取得
## '''
##     q = request.args.get('q', '')
##     return q  # ?q=何ちゃらの何ちゃらが出力される。returnなのに注意。htmlは介してない。

## @app.route('/login', methods=['GET'])
## def render_form():
##     return render_template('login.html')

## # request.formってもしや、formタグ中のinputの中のnameに格納された変数を指定すると受け取れるってことかな
## @app.route('/login', methods=['POST'])
## def login():
##     print("hogerun")
##     if request.form['username'] and request.form['email']:
##         return render_template('check.html', email=request.form['email'], username=request.form['username'])
##     else:
##         return render_template('error.html')
    
## @app.route('/upload', methods=['GET'])
## def render_upload_form():
##     return render_template('upload.html')


## @app.route('/upload', methods=['POST'])
## def upload_file():
##     if request.form['name'] and request.files['image']:
##         print("hoge")
##         f = request.files['image']
##         filepath = 'static/' + secure_filename(f.filename)
##         # secure_filenameは例外辞書に当てはまるものを弾く仕様なのかな
##         print(filepath)
##         f.save(filepath)
##         return render_template('result.html', name=request.form['name'], image_url=filepath)



## # /にアクセスがあった時の処理
## @app.route('/')
## ## def index():
## ##     # scriptタグがそのまま出力されてしまい危険
## ##     return render_template('index.html', unescaped="<script>alert('hoge')</script>")
## ## def index():
## ##     # 辞書データにアクセス
## ##     return render_template('index.html', obj={"title": "hoge"})
## ## def index():
## ##      # 単純に引数をテンプレートに渡す
## ##      return render_template('index.html', title="Hello World")
## # randomで表示ページを変える。
## ## @app.route('/')
## ## def index():
## ##     return render_template('index.html', random=random())
## # loopでリスト表示
## @app.route('/')
## def index():
##     return render_template('index.html', l=["Hoge", "Fuga", "Foo"])
# tableへの辞書型を用いたループ処理
## @app.route('/')
## def index():
##     return render_template('index.html', l=[{"name":"Hoge", "value":"1"}, {"name":"Fuga","value":"2"}, {"name":"Foo", "value":"3" }])
# inheritance implement
@app.route('/')
def index():
    return render_template('index.html', title="Hoge", message="Fuga")

## def hello_world():  # render_templateを使わない時
##     return """
## <!DOCTYPE>
## <html>
## <head>
## <meta charset="utf-8">
## <link rel="stylesheet"
## href="/static/style.css"/>
## </head>
## <body>
## <h1> Hello World</h1>
## </body>
## </html>
## """


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


