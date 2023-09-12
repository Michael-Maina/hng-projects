#!/usr/bin/python3
"""
Users Table Module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    __tablename__ = 'users'

    name = Column(String(128))
