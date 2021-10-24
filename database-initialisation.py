import sqlite3 as sql

conn = sql.connect('MasterDataBase.db')

c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    written INTEGER
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL,
    grade INTEGER,
    FOREIGN KEY (subject_name) REFERENCES subjects (name)
)
""")

conn.commit()

conn.close()
