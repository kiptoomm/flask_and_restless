from sqlalchemy import ForeignKey, Column, Integer, String, Boolean


class MyClass(object):
    first_name = Column(String(64))
    last_name = Column(String(64))

