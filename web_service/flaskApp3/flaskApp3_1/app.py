from flask import Flask, request, make_response, render_template


app = Flask(__name__)


@app.route("/")
def index():
    try:
        count = request.cookies.get("count")
        # Cookieに保存したデータの取得
        if count != None:
            count = int(count) + 1
        else:
            count = 0
        # make_responseはレスポンスオブジェクト(レスポンスを返せるやつ。今回だとrender_template)を引数として与えると、変数として、取得し、セットできる
        resp = make_response(render_template("index.html", count=count))
        # set_cookieは第一引数にキーを第二引数に値をセットできる
        resp.set_cookie("count", str(count))
        return resp
    except Exception as e:
        return render_template("error.html"), 500
                             
