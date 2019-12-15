#!/usr/bin/python3
""" takes name of a state as an argument and lists all cities of that state,
    SQL injection free!
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id=states.id WHERE states.name=%s""",
                (argv[4], ))
    query_rows = cur.fetchall()
    query_ls = []
    for row in query_rows:
        query_ls.append(row[0])
    print(', '.join(query_ls))
    cur.close()
    db.close()
