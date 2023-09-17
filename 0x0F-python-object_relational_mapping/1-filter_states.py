#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    database = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                               passwd=argv[2], db=argv[3])

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
