#!/usr/bin/python3
""" MySQLdb"""
import sys
import MySQLdb

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
