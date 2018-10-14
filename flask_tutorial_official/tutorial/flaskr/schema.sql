--sqlite3 /tmp/flaskr.db < schema.sqlはファイル内に書いちゃダメだよ。sql的に変--
--near "sqlite3": syntax error--
drop table if exists entries;  -- entriesテーブルが存在していたら、dropつまり、テーブルを削除する。テーブルってまあ表みたいなやつ？
create table entries (-- cretate tableでテーブルを作成できる。
       id integer primary key autoincrement,  --column1、データ型integere、primary key指定すると、主キーになる。
       title string not null, -- nullを入れられないってことか
       text string not null
);
