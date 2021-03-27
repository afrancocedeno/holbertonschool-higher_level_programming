#!/usr/bin/python3
"""
prints all data rows from the states table.
"""
if __name__ == "__main__":

    import MySQLdb
    import sys
# use credential as dictionary to code legibility
    credentials = {
        'host': "localhost",
        'port': 3306,
        'user': sys.argv[1],
        'passwd': sys.argv[2],
        'db': sys.argv[3],
        'charset': "utf8"
    }

    query = 'SELECT * FROM states ORDER BY id ASC;'
# traverse the each value as ** for dict
    with MySQLdb.connect(**credentials) as connection:
        # connection = MySQLdb.connect(**credentials)
        # cursor need to habndle the query
        # with statement to avoid cursor_variable = connection.cursor()
        # fetchall returns a tuple with all rows
        with connection.cursor() as cursor:
            cursor.execute(query)
            data_rows = cursor.fetchall()

# connection needs to be closed
# connection.close()

# print the each value as * for list
    print(*data_rows, sep='\n')

# [print(data) for data in table]
