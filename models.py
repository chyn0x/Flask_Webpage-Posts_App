import sqlite3 as sql
from os import path
ROOT = path.dirname(path.relpath((__file__)))

def create_post(name,content):
    con= sql.connect(path.join(ROOT,'database.db'))
    cursor = con.cursor()
    cursor.execute('insert into posts(name,content) values(?, ?)', (name,content))
    con.commit()
    con.close()

def get_posts():
    con= sql.connect(path.join(ROOT,'database.db'))
    cursor = con.cursor()
    cursor.execute('select * from posts')
    posts= cursor.fetchall()
    return posts
