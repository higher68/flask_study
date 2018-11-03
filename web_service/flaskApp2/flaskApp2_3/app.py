# フォームから新しいユーザー情報を入力して、その情報をデータベースに格納sる簡単なデモ
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

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
    def __repr__(self):
        return '<User %r>'% self.username

@app.route('/')
def index():
    users = User.query.all()  # User.queryはデータベースから個別のデータを取り出すのに使う
    return render_template("index.html", users=users)



@app.route('/form')
def forn():
    return render_template("form.html")


@app.route("/register", methods=["POST"])
def register():
    if request.form["username"] and request.form["description"] and request.files["image"]:
        f = request.fils["image"]
        filepath = "static/" + secure_filename(f.filename)
        f.save(filepath)


        filepath= "/" + filepath
        newUser = User(username=request.form["username"], description=request.form["description"], user_image_url=filepath)
        db.session.add(newUser)
        db.session.commit()
        return render_template("result.html", username=request.form["username"], description=request.form["description"])
    else:
        return render_template("error_html")


@app.cli.command("initdb")
def initdb_command():
    db.create_all()
