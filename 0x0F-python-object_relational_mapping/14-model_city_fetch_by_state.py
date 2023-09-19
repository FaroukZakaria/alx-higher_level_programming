#!/usr/bin/python3
""" Print Objects """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":

    Str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(Str.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in (
            session.query(City.name, City.id, State.name)
            .filter(State.id == City.state_id)
            ):
        print("{}: ({}) {}".format(i[0], str(i[1]), i[2]))
    session.close()
