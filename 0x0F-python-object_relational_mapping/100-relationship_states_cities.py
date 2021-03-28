#!/usr/bin/python3
'''
module: relationship state cities

'''
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    '''s
    script that creates the State “California”
    with the City “San Francisco” from the database

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

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Define state name
    new_state_name = 'California'
    new_city_name = 'San Francisco'
    # Create new state
    new_state = State(name=new_state_name)
    new_city = City(name=new_city_name, state=new_state)
    # add new state to sessioin
    session.add(new_city)
    session.commit()


if __name__ == "__main__":
    main()
