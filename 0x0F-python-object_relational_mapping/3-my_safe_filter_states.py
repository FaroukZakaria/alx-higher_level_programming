#!/usr/bin/python3
""" Filter states by user input """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    mask = sys.argv[4]
    cursor.execute("""
        SELECT * FROM states
        WHERE name LIKE BINARY %s
        ORDER BY states.id ASC
    """, (mask, ))
    res = cursor.fetchall()
    for row in res:
        print(row)
    cursor.close()
    db.close()
