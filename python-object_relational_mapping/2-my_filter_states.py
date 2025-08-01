#!/usr/bin/python3
"""takes in an argument and displays all values in the states"""
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
    statename = sys.argv[4]
    query = "SELECT * FROM states WHERE BINARY name LIKE '{}'"\
            "ORDER BY id ASC;"\
            .format(statename)
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
