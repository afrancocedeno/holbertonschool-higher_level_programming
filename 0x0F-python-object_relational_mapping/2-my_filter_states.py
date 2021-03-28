#!/usr/bin/env python3
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

query = '''
        SELECT * FROM states
        WHERE name = '{}'
        ORDER BY id ASC
        '''.format(sys.argv[4])

with MySQLdb.connect(**credentials) as connection:
    with connection.cursor() as cursor:
        cursor.execute(query)
        data_rows = cursor.fetchall()

print(*data_rows, sep='\n')
