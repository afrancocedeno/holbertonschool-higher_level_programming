#!/usr/bin/python3
"""module cities by state"""


def main():
    """
    script that lists all cities from the database hbtn_0e_4_usa
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
            SELECT cities.id, cities.name, states.name
            FROM cities JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC;
            '''

    connection = MySQLdb.connect(**credentials)

    with connection.cursor() as cursor:
        cursor.execute(query)
        data_rows = cursor.fetchall()

    print(*data_rows, sep='\n') if (data_rows) else 0

    connection.close()


if __name__ == "__main__":
    main()
