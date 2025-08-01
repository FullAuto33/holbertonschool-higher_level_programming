#!/usr/bin/python3
"""prints all City objects from the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    resultat = (
        session.query(State.name, City.id, City.name)
        .join(City)
        .order_by(City.id)
        .all()
    )

    for state_name, city_id, city_name in resultat:
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    session.close()
