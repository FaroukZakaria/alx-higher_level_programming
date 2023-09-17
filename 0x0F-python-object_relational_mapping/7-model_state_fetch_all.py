#!/usr/bin/python3
""" All states SQLAlchemy """

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from model_state import Base, State
    import sys

    if len(sys.argv) < 4:
        exit(1)
    Str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(Str.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    base.metadata.create_all(engine)
    session = Session()
    results = session.query(State).order_by(State.id).all()
    for state in results:
        print("{}: {}".format(state.id, state.name))
    session.close()
