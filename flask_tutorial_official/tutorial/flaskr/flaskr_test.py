import os
import flaskr  # flaske.pyをロード
import unittest  # プログラムをテストするためのライブラリ
import tempfile  # 一時ファイルやディレクトリの作成


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
        self.db_fd, flaskr.DATABASE = tempfile.mkstemp()
        self.app = flaskr.app.test_client()
        flaskr.init_db()


    def tearDown(self):
        '''
        一般にテストメソッドが実行され、結果が記録された直後に呼び出されるメソッド
        テスト後のデータベース削除。
        '''
        os.close(self.db)
        os.unlink(flaskr.DATABASE)


if __name__ == '__main__':
    unittest.main()
