"""This module contains; request and response model structure"""
from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    uuid: str
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    city: str
    state: str
    phone: str


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
