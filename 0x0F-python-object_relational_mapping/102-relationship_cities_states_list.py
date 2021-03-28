#!/usr/bin/python3
'''
module: relationship states cities list

'''
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    '''s
    script that lists all State objects, and corresponding
    City objects, contained in the database

    '''

    credentials = (
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(*credentials),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print('{:d}: {:s} -> {:s}'.format(city.id, city.name, city.state.name))


if __name__ == "__main__":
    main()
