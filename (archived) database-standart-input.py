import sqlite3 as sql

conn = sql.connect('MasterDataBase.db')

c = conn.cursor()

c.execute("DELETE FROM subjects")
c.execute("DELETE FROM grades")
c.execute("DELETE FROM semesters")
c.execute("DELETE FROM points")
c.execute("DELETE FROM types")

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
    (9, "Geographie", 50, 50, 0),
    (10, "Ethik", 50, 50, 0),
    (11, "Bildende Kunst", 30, 20, 50),
    (12, "Sport", 50, 50, 0),
    (13, "Seminarkurs", 50, 50, 0),
    (14, "Informatik", 50, 50, 0);
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
    points (id, name)
VALUES
    (1, 15),
    (2, 14),
    (3, 13),
    (4, 12),
    (5, 11),
    (6, 10),
    (7, 9),
    (8, 8),
    (9, 7),
    (10, 6),
    (11, 5),
    (12, 4),
    (13, 3),
    (14, 2),
    (15, 1),
    (16, 0)                    
""")

c.execute("""
INSERT INTO
    types (id, name)
VALUES
    (1, "schriftlich"),
    (2, "mündlich"),
    (3, "spezial")                
""")

conn.commit()

conn.close()
