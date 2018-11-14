from flask import Flask, redirect , url_for, session, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # dbのマイグレーション：dbに保存されたデータを保ったままデータを書き込むこと
# dbは通常では、シャットダウンするごとに入っていたデータは消えていく
from flask_login import UserMixin, LoginManager,
login_user, logout_user, current_user  # Flaskでのユーザセッション管理を効率的に行える。 ユーザのログイン、ログアウト、データベースでのユーザ管理を容易に行える
from datetime import datetime
from rauth import OAuth1Service  # OAuthのライブラリ


app = Flask(__name__)
app.securet_key = "hFSs0cJryVdsISEZzbezsCT64wPOKnOKcqCORAQuUPq5h7Cf2s"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost/hotdb"
db = SQLAlchemy(app)  # Flaskインスタンスを使って、ORMを使えるように。
login_manager = LoginManager(app)  # LoginManageのインスタンス確保
login_manager.login_view = "index"
migrate = Migrate(app, db)

service = OAuth1Service(
    name="twitter",
    consumer_key="rZW4bRMERjEhldc2uAJAImvmU"
    consumer_secret="hFSs0cJryVdsISEZzbezsCT64wPOKnOKcqCORAQuUPq5h7Cf2s"
    request_token_url="https:/api.twitter.com/oauth/request_token",
    authorize_url="https:/api.twitter.com/oauth/authorize",
    access_token_url="https:/api.twitter.com/oauth/access_token",
    base_url="https:/api.twitter.com/1.1")
   
    

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(1024), index=True, unique=True)
    user_image_url = db.Column(db.String(1024), index=True, unique=True)
    date_published = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    twitter_id=db.Column(db.String(64), nullable=False, unique=True)
    def __repr__(self):
        return "<USER %r>" % self.username


@app.route("/")
def index():
    users = User.query.all()

    return render_template("index.html", users=users)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/oauth/twitter")
def oauth_authorize():
    if not current_user.is_anonymous:
        return redirect(url_for("index"))
    else:
        request_token = service.get_request_token(
            params={"oauth_callback":url_for("oauth_callback", provider="twitter", _external=True)}
            )
        return redirect(service.get_authorize_url(request_token[0]))


@app.route("/oauth/twitter/callback")
def oauth_callback():
    request_token = session.pop("request_token")
    oauth_session = service.get_autho_session(
        request_token[0],
        request_token[1],
        data={"oauth_
        
                    
    
    

@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/register", methods=["POST"])
def register():
    if request.form["username"] and request.form["description"] and request.files["image"]:
        f = request.files["image"]
        filepath = 

                         
