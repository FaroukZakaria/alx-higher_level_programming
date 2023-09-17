#!/usr/bin/python3
""" Filter states """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost', user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""
        SELECT * FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY states.id ASC
    """)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
