#!/usr/bin/python3

import MySQLdb
from sys import argv
"""
displays all SQL values where name matches the last argument
MySQL injections proof
"""

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                (sys.argv[4], ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
