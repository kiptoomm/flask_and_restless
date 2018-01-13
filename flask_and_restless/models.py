from enum import Enum
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import backref, relationship
from flask_and_restless import Base

#Gender = Enum('Gender', ['M', 'F', 'U'])
class Gender(Enum):
    MALE = 'M'
    FEMALE = 'F'
    UNKNOWN = 'U'

class Author(Base):
    @declared_attr
    def __tablename__(cls):
        # API endpoint will take the form '/api/__tablename__'
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    first_name = Column(String(64))
    last_name = Column(String(64))
    gender = Column(Enum, default=Gender.UNKNOWN)

class Book(Base):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True) 
    title = Column(String(64))
    author_id = Column(Integer, 
        ForeignKey("author.id"), nullable=True)
    author = relationship(Author, 
        backref=backref('books'))  
    is_available = Column(Boolean)

