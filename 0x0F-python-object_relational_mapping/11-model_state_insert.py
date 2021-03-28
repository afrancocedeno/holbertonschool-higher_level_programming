#!/usr/bin/python3
'''module: model state insert
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    '''script that adds the State object
        “Louisiana” to the database input
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

    # Define state name
    new_state_name = 'Louisiana'
    # Create new state
    new_state = State(name=(new_state_name))
    # add new state to sessioin
    session.add(new_state)
    session.commit()

    print('{:d}'.format(new_state.id))


if __name__ == "__main__":
    main()
