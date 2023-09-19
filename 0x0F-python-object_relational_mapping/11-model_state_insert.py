#!/usr/bin/python3
""" New state """
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
    new_state = State(name='Louisiana')
    session.add(new_state)
    results = session.query(State).filter_by(name='Louisiana').first()
    print(results.id)
    session.commit()
