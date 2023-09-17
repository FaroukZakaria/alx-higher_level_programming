#!/usr/bin/python3
""" All states SQLAlchemy """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
import sys

if len(sys.argv) < 4:
    exit(1)
if __name__ == "__main__":
    engine = create_engine("""
                mysql+mysqldb://{}:{}@localhost:3306/{}
            """.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    session = sessionmaker(bind=engine)
    base.metadata.create_all(engine)
    session1 = Session()
    results = session1.query(State).order_by(State.id).all()
    for state in results:
        print('{}: {}'.format(state.id, state.name))
    session1.close()
