import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def state_list(username, password, dbname):
    # Create a connection to the database
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}")

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_list(username, password, dbname)