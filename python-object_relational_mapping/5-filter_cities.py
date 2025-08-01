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
        """SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;""",
        (sys.argv[4],)
    )

    citys = cursor.fetchall()
    print(", ".join([city[0] for city in citys]))

    cursor.close()
    db.close()
