#!/usr/bin/python3
"""Write a Python file similar to model_state.py named model_city.py"""
import MySQLdb
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    comb = session.query(State, City).order_by(City.id).\
        filter(State.id == City.state_id)
    for rowS, rowC in comb:
        print(f'{rowS.name}: ({rowC.id}) {rowC.name}')

    session.close()
