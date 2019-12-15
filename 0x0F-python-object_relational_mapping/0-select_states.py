#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
"""
<<<<<<< HEAD


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], 
                    db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM state ORDERED BY id")
    query_rows = db.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
=======
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
>>>>>>> ac232a94564604d24fc7c17c5fb45f9621392988
