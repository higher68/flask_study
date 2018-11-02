from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/hestdv"
db = SQLAlchemy(app)
# ORMで言語のクラスとテーブルを結びつけるためのモデル
class User(db.Model):  # db.Modelを継承
    id = db.Column(db.Integer, primary_key=True)  # ユーザをデータベース、アプリ内部で区別するための固有番号
    # 第一引数がデータ構造。これに合わないものが挿入されるとエラーを吐く, primary_keyはデータを挿入した順に通し番号が振られるってこと。
    username = db.Column(db.String(64), index=True, unique=True)
    # ユーザーの名前、unique=Trueでデータの重複を防げる
    description = db.Column(db.String(120), index=True, unique=True)
    user_image_url = db.Column(db.String(120), index=True, unique=True)
    def __repr__
conn = psycopg2.connect("dbname=testdb")  # databaseへのconnctionを作成
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)  # connectionを作ったdatabaへのカーソルの作成

@app.route('/', methods=['GET'])
def index():
    ''' form入力するとdatabaseが更新され、その結果が'/'に反映、表示される
'''
    cur.execute("SELECT* FROM messages;")  # これで、デーブルのデータを取り出すと、カーソルからSQLの実行ができるようになる
    messages = cur.fetchall()
    messages = [ dict(message) for message in messages]  # messageのdict作成
    return render_template('index.html', messages=messages)  # dictのレンダリングtoindex

# /postのGETでformを表示、その中で、POSTを要求した時、POSTに飛んで、request.formが実行って感じ？
@app.route('/post', methods=['GET'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        try:
            cur.execute("INSERT INTO messages (username, message) VALUES(%s, %s)",
                        (request.form['username'], request.form['message']))  # htmlのinputから値を取り出し、SQL実行でデータベースに反映
            # 上で、inputした文字列をそのまま文字列に入れ込まず、テンプレートから文字列を引っ張ってきてる？プリペアドステートメント
            # プリペアドステートメントとは、テンプレのSQL文を最初に用意して置いて、あとはその中の変数だけを変更して、クエリを実行できる機能状態
            # request.formの意味がよくわからん
            conn.commit  # 処理の確定

            return render_template('result.html',
                                   username=request.form['username'],message=request.form['message'])
        # form.htmlから値を取り出し、それをresult.htmlにレンダリンぐ
        except Exception as e :  # Exceptionクラスというのがあるらしい Exceptionを渡すと、すべての例外を受け取れるらしい
            # except 例外形 as 変数名とすると、例外を受け取れる
            return render_template('error.html')

        
@app.route('/answer')
def answer():
    return render_template('answer.html')
