#!/usr/bin/python3
""" First state """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":

    Str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(Str.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in session.query(State).filter(State.name.like('%a%')):
        print(i.id, i.name, sep=': ')
