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
            SELECT cities.name FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name LIKE %s
            ORDER BY cities.id ASC;
            '''

    connection = MySQLdb.connect(**credentials)

    with connection.cursor() as cursor:
        cursor.execute(query, (sys.argv[4], ))
        data_rows = cursor.fetchall()

    # inline print using join
    [print(', '.join([str(data[0]) for data in data_rows]))]\
        if (data_rows) else 0

    connection.close()


if __name__ == "__main__":
    main()
