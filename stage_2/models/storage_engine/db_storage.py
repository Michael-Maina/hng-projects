#!/usr/bin/python3
"""
SQL Database Storage Module
"""
from dotenv import load_dotenv
from models.base_model import Base
from models.users import User
from os import getenv
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, scoped_session
from typing import Dict, Union

load_dotenv()


class DBStorage():

    __session = None
    __engine = None

    def __init__(self) -> None:
        username = getenv('DB_USERNAME')
        password = getenv('DB_PWD')
        host = getenv('DB_HOST')
        db = getenv('DB_DATABASE')

        self.__engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@{host}/{db}',
            pool_pre_ping=True)

    def new(self, obj) -> None:
        """ Adds new record to database """
        self.__session.add(obj)

    def save(self) -> None:
        """ Commits transaction to database """
        self.__session.commit()

    def delete(self, obj) -> None:
        """ Deletes record from database """
        self.__session.delete(obj)
        self.save()

    def reload(self) -> None:
        """
        Sets up the database schema by creating tables if they don't exist,
        and creating a session for interacting with the database.
        """
        Base.metadata.create_all(self.__engine)
        sesh = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesh)
        self.__session = Session()

    def get_record(self, name=None, id=None) -> Union[str, None]:
        """ Returns a record from the database """
        if name:
            stmt = select(User).where(User.name == name)
            user = self.__session.scalars(stmt).first()
            return user
        elif id:
            stmt = select(User).where(User.id == id)
            user = self.__session.scalars(stmt).first()
            return user

        return None

    def close(self) -> None:
        self.__session.close()
