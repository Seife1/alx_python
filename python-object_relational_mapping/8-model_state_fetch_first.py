#!/usr/bin/python3
"""
A script that prints the first State object from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def state_list_first(username, password, dbname):
    # Create a connection to the database
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}")

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_list_first(username, password, dbname)