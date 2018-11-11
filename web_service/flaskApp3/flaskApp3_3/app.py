from flask import Flask, redirect , url_for, session, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # dbのマイグレーション：dbに保存されたデータを保ったままデータを書き込むこと
# dbは通常では、シャットダウンするごとに入っていたデータは消えていく
from flask_login import UserMixin, LoginManager,
login_user, logout_user, current_user  # Flaskでのユーザセッション管理を効率的に行える。 ユーザのログイン、ログアウト、データベースでのユーザ管理を容易に行える
from datetime import datetime
from rauth import OAuthlService  # OAuthのライブラリ


app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost/testdb"
db = SQLAlchemy(app)  # Flaskインスタンスを使って、ORMを使えるように。
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(120), index=True, unique=True)
    user_image_url = db.Column(db.String(120), index=True, unique=True)
    date_published = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return "<USER %r>" % self.username


@app.route("/")
def index():
    users = User.query.all()
