#!/usr/bin/python3
'''module: model state my get
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    '''script that prints the State object with the
        name passed as argument from the database
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

    data_filter = session.query(State).\
        filter(State.name.like(sys.argv[4])).all()

    [print("{:d}".format(data.id)) for data in data_filter]\
        if (data_filter) else print('Not found')


if __name__ == "__main__":
    main()
