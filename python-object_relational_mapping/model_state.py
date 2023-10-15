"""SQLAlchemy ORM"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import Session, declarative_base


Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://'root':'123abcSEI'@'localhost:3306/tutor'")

    Base.metadata.create_all(engine)

    session = Session(bind=engine)
