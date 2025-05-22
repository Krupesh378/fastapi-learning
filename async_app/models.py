"""This module configuration with the models schemas"""
from sqlalchemy import Column, Integer, String, DateTime
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    city = Column(String)
    state = Column(String)
    phone = Column(String)
    dob = Column(DateTime)
