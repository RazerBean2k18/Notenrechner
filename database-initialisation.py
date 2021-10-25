import sqlite3 as sql

conn = sql.connect('MasterDataBase.db')

c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    written_weight INTEGER,
    oral_weight INTEGER,
    FOREIGN KEY (written_weight) REFERENCES weighting (value),
    FOREIGN KEY (oral_weight) REFERENCES weighting (value)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL,
    grade INTEGER,
    weightng_type TEXT NOT NULL,
    semester TEXT,
    FOREIGN KEY (subject_name) REFERENCES subjects (name),
    FOREIGN KEY (semester) REFERENCES semesters (name)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS semesters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS weighting (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value INTEGER
)
""")

conn.commit()

conn.close()
