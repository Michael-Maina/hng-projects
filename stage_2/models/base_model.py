#!/usr/bin/python3
"""
Base Class for Database Storage
"""
from datetime import datetime, timezone
from sqlalchemy import DateTime, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from typing import Dict

Base = declarative_base()


class BaseModel():

    id = Column(Integer(), primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return (f"[{self.__class__.__name__} {self.id} {self.__dict__}]")

    def save(self) -> None:
        """ Saves a new object in the database """
        from models import storage
        self.updated_at = datetime.now(timezone.utc)
        storage.new(self)
        storage.save()

    def to_dict(self) -> Dict:
        """ Returns all attributes of an object """
        obj_dict = self.__dict__.copy()
        del obj_dict['created_at']
        del obj_dict['updated_at']
        del obj_dict['_sa_instance_state']
        return obj_dict
