#!/usr/bin/python3
""" Filter states by user input """
import MySQLdb
import sys

if name == "__main__":
    db = MySQLdb.connect(
            host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""
        SELECT * FROM states
        WHERE name LIKE {}
        ORDER BY states.id ASC
    """.format(sys.argv[4]))
    res = cursor.fetchall()
    for row in res:
        print(row)
    cursor.close()
    db.close()
