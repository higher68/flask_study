from flask import Flask  # Flaskクラスのインポート
# WSGIアプリケーションとなるらしい。WEBサーバとアプリケーションを接続するためのインターフェースをPythonで定義したもの
# WebサーバとWebアプリの実装を切り離し、柔軟に組み合わせられる。らしい。
# https://qiita.com/habakan/items/67fb25c34a35db373c07
# add_url_ruleメソッドをdecorator()を通して実行しているらしい。
# add_url_rule()を実行して、hello()が実行される。
# アプリとして起動したときは、__name__の中身は__main__、モジュールとしてインポートされたときは、ファイル名となる
app = Flask(__name__)  # インスタンスの生成 Flaskがどこからファイルを探すかを認識するのに必要らしいが。うーん￥？
# この場合は、Flask.route()メソッドにデコレートしてる。
# route関数の詳細は下。
# 今回は、デコレートする時に、add_url_ruleが実行されてる。
## def route(self, rule, **options):
##     """A decorator that is used to register a view function for a
##     given URL rule.  This does the same thing as :meth:`add_url_rule`
##     but is intended for decorator usage::

##         @app.route('/')
##         def index():
##             return 'Hello World'

##     For more information refer to :ref:`url-route-registrations`.

##     :param rule: the URL rule as string
##     :param endpoint: the endpoint for the registered URL rule.  Flask
##                      itself assumes the name of the view function as
##                      endpoint
##     :param options: the options to be forwarded to the underlying
##                     :class:`~werkzeug.routing.Rule` object.  A change
##                     to Werkzeug is handling of method options.  methods
##                     is a list of methods this rule should be limited
##                     to (``GET``, ``POST`` etc.).  By default a rule
##                     just listens for ``GET`` (and implicitly ``HEAD``).
##                     Starting with Flask 0.6, ``OPTIONS`` is implicitly
##                     added and handled by the standard request handling.
##     """
    ## def decorator(f):
    ##     endpoint = options.pop('endpoint', None)
    ##     self.add_url_rule(rule, endpoint, f, **options)
    ##     return f
    ## return decorator


@app.route('/')  # デコレータ。これを使うと関数を簡単に上書きできる
 def hello_world():
     return "Hello World!"

# def hello_world():
#    return "Hello World!"
# hello_world = app.route('/', hello_world())
# と同等

if __name__ == '__main__':
    app.run()  # ローカルサーバでアプリを実行
    
