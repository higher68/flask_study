import os
import flaskr  # flaske.pyをロード
import unittest  # プログラムをテストするためのライブラリ
import tempfile  # 一時ファイルやディレクトリの作成
import os
# print("hoho")
os.system('sqlite3 /tmp/flaskr.db < schema.sql')
# print("hohoge")
# class クラス名前(親クラス)とすると、新しいクラスはサブクラスにんる
# TestCaseクラスはunittestの世界での論理的なテストの単位。
# TestCaseクラスをベースとして必要なテストをサブクラスに実装する。
class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        '''
        一般にテストフィクスチャ(テストを実行・成功させるための必要な前提・状態の集合)
        の準備のために呼び出されるメソッド
        新しいテクストクライアントを作成、新しいデータベースを初期化
        '''
        # 低レベルなファイルハンドルと、データベース名を返す？
        # mkstempで作ったファイルはユーザーが手動で削除する必要あり
        # mkstemp()の戻りは、ファイル値とファイルの絶対パス
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        self.app = flaskr.app.test_client()
        with flaskr.app.app_context():
            flaskr.init_db()

        
    def tearDown(self):
        '''
        一般にテストメソッドが実行され、結果が記録された直後に呼び出されるメソッド
        テスト後のデータベース削除。
        '''
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])


    def test_empty_db(self):
        '''
        アプリのルート=「\」にアクセスすると、アプリが"No entries here so far"を表示することをチェック
'''
        rv = self.app.get('/')  # self.app.gethttp getリクエストを特定のパスがあるアプリに送る
        # print(rv)
        # GETはWebサーバに値を送る時にURLの後ろにくっつけておくる。何かを取得する時に使う
        # POSTは値を見えないところに隠しておくる?何かを新しく登録する時に使う
        assert b'No entries here so far' in rv.data  # 条件がTrue出ない時に例外を投げるんだってさ。

    def login(self, username, password):
        '''正直app.postがよくわからんが、おそらく
1st引数に、アドレス、第二に渡すもの、第三はまあリダイレクトだから、post or getした後で、ページに飛ぶってことか？
        '''
        return self.app.post('/login', data=dict(
            username=username,
            password=password
            ), follow_redirects=True)

   
    def logout(self):
        return self.app.get('/logout', follow_redirects=True)


    def test_login_logout(self):
        # login、logoutが正常終了するか
        rv = self.login('admin', 'default')
        assert b'You were logged in' in rv.data
        rv = self.logout()
        assert b'You were logged out' in rv.data
        # login、logoutが正常失敗するか
        rv = self.login('adminx', 'default')
        assert b'Invalid username' in rv.data
        rv = self.login('admin', 'dafaultx')
        assert b'Invalid password' in rv.data


    def test_messages(self):
         self.login('admin', 'default')
         rv = self.app.post('/add', data=dict(
             title='<Hello>',
             text='<strong>HTML</strong> allowed here'),
                            follow_redirects=True)
         assert b'No entries here so far' not in rv.data
         assert b'&lt;Hello&gt;' in rv.data
         assert b'<strong>HTML</strong> allowed here' in rv.data





if __name__ == '__main__':
    unittest.main()
