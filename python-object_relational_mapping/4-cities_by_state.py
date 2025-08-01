#!/usr/bin/python3
"""lists all cities from the database"""
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
        """SELECT cities.id, cities.name, states.name
           FROM cities
           JOIN states ON cities.state_id = states.id
           ORDER BY cities.id ASC"""
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
