#!/usr/bin/python3
"""module my_safe_filter_states"""


def main():
    """
    write one that is safe from MySQL injections!
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

    query = '''
            SELECT * FROM states
            WHERE name LIKE %s
            ORDER BY id ASC;
            '''

    connection = MySQLdb.connect(**credentials)

    with connection.cursor() as cursor:
        cursor.execute(query, (sys.argv[4], ))
        data_rows = cursor.fetchall()

    print(*data_rows, sep='\n') if (data_rows) else 0

    connection.close()


if __name__ == "__main__":
    main()
