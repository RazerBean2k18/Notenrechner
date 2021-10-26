import sqlite3 as sql

conn = sql.connect('MasterDataBase.db')

c = conn.cursor()

c.execute("""
INSERT INTO
    subjects (id, name, written_weight, oral_weight, special_weight)
VALUES
    (1, "Wirtschaft", 50, 50, 0),
    (2, "Englisch", 50, 50, 0),
    (3, "Mathe", 66, 33, 0),
    (4, "Deutsch", 50, 50, 0),
    (5, "Biologie", 50, 50, 0),
    (6, "Physik", 60, 40, 0),
    (7, "Geschichte", 50, 50, 0),
    (8, "Gemeinschaftskunde", 50, 50, 0),
    (9, "Ethik", 50, 50, 0),
    (10, "Bildende Kunst", 30, 20, 50),
    (11, "Sport", 50, 50, 0),
    (12, "Seminarkurs", 50, 50, 0),
    (13, "Informatik", 50, 50, 0);
""")

c.execute("""
INSERT INTO
    semesters (id, name)
VALUES
    (1, "Halbjahr I"),
    (2, "Halbjahr II"),
    (3, "Halbjahr III"),
    (4, "Halbjahr IV");
""")

c.execute("""
INSERT INTO
    weighting (id, value)
VALUES
    (1, 20),
    (2, 30),
    (3, 33),
    (4, 40),
    (5, 50),
    (6, 60),
    (7, 66);
""")

conn.commit()

conn.close()
