#!/usr/bin/python3
'''
module: model state update id

'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    '''
    script that changes the name of a State
    object from the database hbtn_0e_6_usa

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

    # update name by id
    ref_id = 2
    new_state_name = 'New Mexico'

    # .one() select directly the mathch
    new_data = session.query(State).filter(State.id.like(ref_id)).one()
    new_data.name = new_state_name

    session.commit()


if __name__ == "__main__":
    main()
