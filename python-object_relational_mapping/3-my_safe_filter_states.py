#!/usr/bin/python3
""" takes in arguments and displays all values in the states"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute(
        """SELECT * FROM states
        WHERE BINARY name LIKE %s
        ORDER BY id ASC""",
        (sys.argv[4],)
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
