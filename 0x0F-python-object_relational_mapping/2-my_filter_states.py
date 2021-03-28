#!/usr/bin/python3
from MySQLdb import Connection


def main():
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

    connection = MySQLdb.connect(**credentials)

    with connection.cursor() as cursor:
        cursor.execute(query)
        data_rows = cursor.fetchall()

    connection.close()

    print(*data_rows, sep='\n')


if __name__ == "__main__":
    # don´t run when imported using class/def
    # source link: t.ly/4Tx3
    main()
