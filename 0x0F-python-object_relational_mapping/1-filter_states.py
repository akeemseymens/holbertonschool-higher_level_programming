#!/usr/bin/python3
""" Script that lists all states with a name starting with N (upper N) from the database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":

        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=arg[2], 
                        db=arg[3], charset="utf8")
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
        query_rows = db.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        db.close()