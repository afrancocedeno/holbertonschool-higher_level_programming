#!/usr/bin/python3
'''
module: model city fetch state

'''
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    '''
    script that prints all City objects from the database

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
    # .all() select directly the mathch
    new_data = session.query(State.name, City.id, City.name)\
        .join(City, State.id.like(City.state_id))\
        .order_by(City.id)\
        .all()

    [print('{:s}: ({:d}) {:s}'.format(*data)) for data in new_data]


if __name__ == "__main__":
    main()
