from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# engine = create_engine('sqlite:///dictionary.db')
engine = create_engine(
    'mysql+pymysql://root:example@localhost:3306/dictionary')


def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
