from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func

Base = declarative_base()


class Dictionary(Base):
    __tablename__ = 'dictionary'
    id = Column(Integer, primary_key=True)
    word = Column(String(255))
    detail = Column(String(255))
    pronounce = Column(String(255))

    @classmethod
    def get_random_words(cls, session, limit=5):
        words = session.query(cls).order_by(func.random()).limit(limit).all()
        session.close()
        return words
