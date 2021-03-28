#!/usr/bin/python3
'''module: model_state_fetch_all
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """script that lists all State objects from the database hbtn_0e_6_usa
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

    all_data = session.query(State).order_by(State.id)

    [print("{:d}: {:s}".format(data.id, data.name)) for data in all_data]


if __name__ == "__main__":
    main()
