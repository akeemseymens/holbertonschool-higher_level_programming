#!/usr/bin/python3

import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", port=3360, user=argv[1], passwd=arg[2], 
                    db=arg[3], charset="utf8")
if __name__ == "__main__":
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states ON cities.state_id=states.id""")
    query_rows = db.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()