#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter a from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def state_list_a(username, password, dbname):
    # Create a connection to the database
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}")

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like("%a%")).all()
    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_list_a(username, password, dbname)