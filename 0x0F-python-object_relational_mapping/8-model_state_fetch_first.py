#!/usr/bin/python3
""" All states SQLAlchemy """

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    Str = 'mysql+mysql://{}:{}@localhost:3306/{}'
    engine = create_engine(Str.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).first()
    if results is None:
        print("Nothing")
    else:
        print(results.id, results.name, sep=": ")
