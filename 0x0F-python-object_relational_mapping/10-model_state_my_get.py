#!/usr/bin/python3
"""prints the State object with the name passed as argument"""
import MySQLdb
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    arg = argv[4]
    line = session.query(State).filter_by(name=arg).first()
    if line is not None:
        print(line.id)
    else:
        print("Not found")

    session.close()
