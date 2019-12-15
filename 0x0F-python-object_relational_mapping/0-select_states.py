#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", port=3360, user=argv[1], passwd=argv[2], 
                    db=argv[3], charset="utf8")
if __name__ == "__main__":
    cur = db.cursor()
    cur.execute("SELECT * FROM state ORDERED BY id")
    query_rows = db.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
