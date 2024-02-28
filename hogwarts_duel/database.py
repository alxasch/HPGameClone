import sqlite3

def add_to_database_1(p1):
    con = sqlite3.connect("data/bd/database_stats")
    cur = con.cursor()

    if p1 == 'garri':
        harry_wins = cur.execute("""SELECT harry FROM stats""").fetchall()
        cur.execute("""UPDATE stats SET harry = harry + 1""")
        print(cur.execute("""SELECT harry FROM stats""").fetchall())
        con.commit()

    if p1 == 'ron':
        harry_wins = cur.execute("""SELECT ron FROM stats""").fetchall()
        cur.execute("""UPDATE stats SET ron = ron + 1""")
        print(cur.execute("""SELECT ron FROM stats""").fetchall())
        con.commit()

    if p1 == 'germiona':
        harry_wins = cur.execute("""SELECT germiona FROM stats""").fetchall()
        cur.execute("""UPDATE stats SET germiona = germiona + 1""")
        print(cur.execute("""SELECT germiona FROM stats""").fetchall())
        con.commit()

    if p1 == 'drako':
        harry_wins = cur.execute("""SELECT draco FROM stats""").fetchall()
        cur.execute("""UPDATE stats SET draco = draco + 1""")
        print(cur.execute("""SELECT draco FROM stats""").fetchall())
        con.commit()
    con.close()


def get_the_value():
    con = sqlite3.connect("data/bd/database_stats")
    cur = con.cursor()
    count = []
    for name in ['germiona', 'harry', 'draco', 'ron']:
        qwe = cur.execute(f'SELECT {name} FROM stats').fetchall()
        con.commit()
        count.append(qwe[0][0])
    con.close()
    return count