import enum
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean
from sqlalchemy.orm import backref, relationship
from flask_and_restless import db

#Gender = Enum('Gender', ['M', 'F', 'U'])
class Gender(enum.IntEnum):
    MALE = 0
    FEMALE = 1
    UNKNOWN = 2

class BaseModel(db.Model):
    '''
    defines an abstract base model from which all project modules inherit
    common fields and methods
    '''
    __abstract__ = True

class Author(BaseModel):
    @declared_attr
    def __tablename__(cls):
        # API endpoint will take the form '/api/__tablename__'
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    first_name = Column(String(64))
    last_name = Column(String(64))
    gender = db.Column(db.Enum(Gender), default=Gender.UNKNOWN)

class Book(db.Model):
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

