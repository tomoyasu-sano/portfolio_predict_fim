    """
    ・sqlite3のdbを作成後
    ・dbからdf.pickleを作成
    
    """

import sqlite3
import pandas as pd
import pandas.io.sql as psql

db_name = './fim_db.sqlite3'

#コネクタ作成：dbnameの名前をもつDBへ接続
conn = sqlite3.connect(db_name)

query = """
select * from fim_data;
"""

df = pd.read_sql(query, conn)
df.to_pickle("./create_model/data/df.pickle")