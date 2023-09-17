#!/usr/bin/python3
""" Classes ORM """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    """ State class """

    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name =  Column(String(128), nullable=False)
