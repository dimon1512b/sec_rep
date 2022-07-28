"""
Mapping - transfer sql objects to python objects
"""
from sqlalchemy import Column
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column()
    name = Column()
    password = Column()
