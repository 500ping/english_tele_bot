from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///dictionary.db')


def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
