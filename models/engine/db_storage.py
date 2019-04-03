#!/usr/bin/python3
"""SQL db engine class"""
import json
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import state
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """SQL db class"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                     .format(os.getenv("HBNB_MYSQL_USER"),
                                     os.getenv("HBNB_MYSQL_PWD"),
                                     os.getenv("HBNB_MYSQL_HOST"),
                                     os.getenv("HBNB_MYSQL_DB")),
                                     pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """All"""
        res = {}
        if cls is not None:
            
        return res

    def new(self, obj):
        """New"""
        self.__session.add(obj)

    def save(self):
        """Save"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload"""
        Base.metadata.create_all(self.__engine)
        current = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(current)
