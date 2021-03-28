#!/usr/bin/python3
"""
    script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
"""


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

    print(*data_rows, sep='\n') if (data_rows) else 0


if __name__ == "__main__":
    # don´t run when imported using class/def
    # source link: t.ly/4Tx3
    main()
