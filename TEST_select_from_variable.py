from sqlite3 import *
import sqlite3 as sq

conn = connect('MasterDataBase.db')

global fach
fach = "Biologie"

cur = conn.cursor()

def get_grades():
    global fach
    select = "SELECT subject_name, grade FROM grades WHERE subject_name LIKE '" + fach + "'"
    for row in cur.execute(select):
        print(row)

get_grades()

conn.commit()
