import os
import flaskr  # flaske.pyをロード
import unittest  # プログラムをテストするためのライブラリ
import tempfile  # 一時ファイルやディレクトリの作成
import os
print("hoho")
os.system('sqlite3 /tmp/flaskr.db < schema.sql')
print("hohoge")
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
        flaskr.init_db()


    def tearDown(self):
        '''
        一般にテストメソッドが実行され、結果が記録された直後に呼び出されるメソッド
        テスト後のデータベース削除。
        '''
        os.close(self.db_fd)
        os.unlink(flaskr.DATABASE)

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
        return self.app.post('/login', data=dict(
            username=username,
            password=password
            ), follow_redirects=True)


    def logout(self):
        return self.app.get('/logout', follow_redirects=True)


if __name__ == '__main__':
    unittest.main()
