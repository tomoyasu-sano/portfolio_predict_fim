"""
making db and table from csv data

data create_model/data/fim_data.csv
１）csvのdataの「カラム」と「一番上のデータ」を切り取る
２）下記のquery tableにtable定義、query_valueに試しのデータとして、１）の「一番上のデータ」をセット
３）このファイルをコマンドラインで叩く（python create_db.py)
４）コマンドラインで、sqlite3 fim_db.sqlite3　でsqlite3の中に入る
５）テーブル確認後、１）のcsvファイルを挿入)
    .mode csv
    .import csvfileの絶対path fim_data
６）fim_data テーブルにデータ挿入を確認
"""


import sqlite3
#接続先のDBの名前設定
db_name = 'fim_db.sqlite3'
#table_name = "fim_data"

#コネクタ作成：dbnameの名前をもつDBへ接続
conn = sqlite3.connect(db_name)
#カーソルの取得
cur = conn.cursor()





query_table = "create table fim_data(id int primary key not null,sex int not null, age int not null, disease int not null, pre_hospitalization_status int not null, days int not null, family int not null, helper int not null, motivation int not null,\
            meal intger not null, hygienic intger not null, wipingClean intger not null, upperBodyDressing intger not null, \
            lowerBodyDressing intger not null, toiletAction intger not null,  urinationControl intger not null, defecationControl intger not null, \
            bedsChairsWheelchairs intger not null, toilet intger not null, bathtubShower intger not null, walkingWheelchair intger not null, stairs intger not null, \
            understanding intger not null, expression intger not null, socialCommunication intger not null, problemSolving intger not null, memory intge not null, \
            discharge int not null,\
            meal_after_1M intger not null, hygienic_after_1M intger not null, wipingClean_after_1M intger not null, upperBodyDressing_after_1M intger not null, \
            lowerBodyDressing_after_1M intger not null, toiletAction_after_1M  intger not null, urinationControl_after_1M intger not null, defecationControl_after_1M  intger not null, \
            bedsChairsWheelchairs_after_1M intger not null, toilet_after_1M intger not null, bathtubShower_after_1M intger not null, walkingWheelchair_after_1M intger not null, \
            stairs_after_1M intger not null, understanding_after_1M intger not null, expression_after_1M intger not null, socialCommunication_after_1M intger not null, \
            problemSolving_after_1M intger not null, memory_after_1M intger not null, \
            \
            meal_after_2M intger not null, hygienic_after_2M intger not null, wipingClean_after_2M intger not null, upperBodyDressing_after_2M intger not null, \
            lowerBodyDressing_after_2M intger not null, toiletAction_after_2M  intger not null, urinationControl_after_2M intger not null, defecationControl_after_2M  intger not null, \
            bedsChairsWheelchairs_after_2M intger not null, toilet_after_2M intger not null, bathtubShower_after_2M intger not null, walkingWheelchair_after_2M intger not null, \
            stairs_after_2M intger not null, understanding_after_2M intger not null, expression_after_2M intger not null, socialCommunication_after_2M intger not null, \
            problemSolving_after_2M intger not null, memory_after_2M intger not null, \
            \
            meal_after_3M intger not null, hygienic_after_3M intger not null, wipingClean_after_3M intger not null, upperBodyDressing_after_3M intger not null, \
            lowerBodyDressing_after_3M intger not null, toiletAction_after_3M  intger not null, urinationControl_after_3M intger not null, defecationControl_after_3M  intger not null, \
            bedsChairsWheelchairs_after_3M intger not null, toilet_after_3M intger not null, bathtubShower_after_3M intger not null, walkingWheelchair_after_3M intger not null, \
            stairs_after_3M intger not null, understanding_after_3M intger not null, expression_after_3M intger not null, socialCommunication_after_3M intger not null, \
            problemSolving_after_3M intger not null, memory_after_3M intger not null  \
            )"

query_value = "insert into fim_data values(1,2,71,2,4,4,2,1,3,5,5,4,4,3,3,4,4,5,3,3,4,3,5,5,5,4,4,1,6,6,5,4,4,3,4,4,5,3,3,4,3,6,5,5,4,5,6,6,7,7,5,5,6,7,7,5,3,6,4,7,7,6,6,6,7,7,7,7,6,5,6,7,7,6,6,7,6,7,7,7,6,7)"



cur.execute(query_table)
cur.execute(query_value)


conn.commit()
conn.close()


