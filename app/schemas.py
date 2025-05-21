"""This module contains like how to request and response structure can be set."""
from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: str


class ItemCreate(ItemBase):
    ...


class Item(ItemBase):
    id: int

    class config:
        orm_mode = True
