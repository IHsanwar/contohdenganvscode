import sqlite3 ,os.path


def sqlconnect():
    db_file = 'library.db'
    print(os.path.isfile(db_file))
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except ValueError as e:
        print(e)

    return conn

def sqlquery(query , conn):
    cur = conn.cursor()

    cur.execute(query)
    return cur

def sqlfetch(cur):
    rows = cur.fetchall()
    return rows