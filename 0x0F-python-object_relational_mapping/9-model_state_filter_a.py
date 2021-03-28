#!/usr/bin/python3
'''module: model_state_filter_a
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """lists all State objects that contain the letter 'a' from the database
    """

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
        order_by(State.id).\
        filter(State.name.like('%a%'))

    [print("{:d}: {:s}".format(data.id, data.name)) for data in data_filter]


if __name__ == "__main__":
    main()
