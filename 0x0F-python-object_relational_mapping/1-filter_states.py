#!/usr/bin/python3
"""
script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

credentials = {
    'host': "localhost",
    'port': 3306,
    'user': sys.argv[1],
    'passwd': sys.argv[2],
    'db': sys.argv[3],
    'charset': "utf8"
}

query = 'SELECT * FROM states WHERE name REGEXP \'^[N]\' ORDER BY id ASC;'

connection = MySQLdb.connect(**credentials)

with connection.cursor() as cursor:
    cursor.execute(query)
    data_rows = cursor.fetchall()

connection.close()
print(*data_rows, sep='\n') if (data_rows) else 0
