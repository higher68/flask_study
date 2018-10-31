from flask import Flask, request, render_template
import psycopg2
import psycopg2.extras

app = Flask(__name__)
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
