#!/usr/bin/python3
'''
module: model state delete a

'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    '''
    script that deletes all State objects with a
    name containing the letter a from the database

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
    new_data = session.query(State).filter(State.name.like('%a%')).all()

    [session.delete(data) for data in new_data]

    session.commit()


if __name__ == "__main__":
    main()
