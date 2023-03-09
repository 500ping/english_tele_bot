from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Dictionary(Base):
    __tablename__ = 'dictionary'
    id = Column(Integer, primary_key=True)
    word = Column(String(255))
    detail = Column(String(255))
