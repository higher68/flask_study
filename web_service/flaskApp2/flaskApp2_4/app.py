# フォームから新しいユーザー情報を入力して、その情報をデータベースに格納sる簡単なデモ
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # ちょっと意味わからんdefaultはfalseらしい
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/testdb"  # dbのURI.データベースにアクセスするために必要
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # flaskとSQLAlchemyをMigrateにセットすることで、使えるようになる。
# ORMで言語のクラスとテーブルを結びつけるためのモデル
# 最初のdb.Columnで、テーブルの中身を設定してる。
class User(db.Model):  # db.Modelを継承
    id = db.Column(db.Integer, primary_key=True)  # ユーザをデータベース、アプリ内部で区別するための固有番号
    # 第一引数がデータ構造。これに合わないものが挿入されるとエラーを吐く, primary_keyはデータを挿入した順に通し番号が振られるってこと。
    username = db.Column(db.String(64), index=True, unique=True)
    # ユーザーの名前、unique=Trueでデータの重複を防げる
    description = db.Column(db.String(120), index=True, unique=True)
    user_image_url = db.Column(db.String(120), index=True, unique=True)
    date_published =  db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self):
        return '<User %r>' % self.username  # instanceの出力。って何？

@app.route('/')
def index():
    users = User.query.all()  # User.queryはデータベースから個別のデータを取り出すのに使う
    return render_template("index.html", users=users)



@app.route('/form')
def form():
    return render_template("form.html")


@app.route("/register", methods=["POST"])
def register():
    # print('hogeta')
    if request.form['username'] and request.form['description'] and request.files['image']:
        # print("hogeo")
        f = request.files["image"]
        filepath = "static/" + secure_filename(f.filename)
        f.save(filepath)
        filepath= "/" + filepath
        # print("geeeee")
        newUser = User(username=request.form["username"], description=request.form["description"], user_image_url=filepath)
        db.session.add(newUser)
        # print('hooooo',newUser.username, newUser.description, newUser.user_image_url)
        # print(newUser)
        db.session.commit()
        # print("ararara")
        return render_template("result.html", username=request.form["username"], description=request.form["description"])
    else:
        return render_template("error_html")


## @app.cli.command("initdb")  # 高設定するとflask initdbでメソッドが使える
## def initdb_command():
##     db.create_all()  # これを行うと、モデルからデータベースの操作を行うことができるようになる。必ずやる
