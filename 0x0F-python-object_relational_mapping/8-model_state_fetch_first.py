#!/usr/bin/python3
"""first State object from the database hbtn_0e_6_usa"""
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

    line = session.query(State).first()
    if line is not None:
        print(f'{line.id}: {line.name}')
    else:
        print("Nothing")

    session.close()
