import sqlite3 as sql

conn = sql.connect('MasterDataBase.db')

c = conn.cursor()

conn.close()
