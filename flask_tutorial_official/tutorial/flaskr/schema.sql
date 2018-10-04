drop table if exists entries:  -- entriesテーブルが存在していたら、dropつまり、テーブルを削除する。テーブルってまあ表みたいなやつ？
create tabele entries { -- cretate tableでテーブルを作成できる。
       id integer primary key autoincrement,  --column1、データ型integere、primary key指定すると、主キーになる。
       title string not null, -- nullを入れられないってことか
       text string not null
};
