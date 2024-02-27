#!/usr/bin/python3
""" This module defines a class to manage db storage for hbnb clone"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """This class manages storage of hbnb models"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        # Retrieve MySQL connection information from environment variables
        mysql_user = getenv("HBNB_MYSQL_USER")
        mysql_password = getenv("HBNB_MYSQL_PWD")
        mysql_host = getenv("HBNB_MYSQL_HOST", default="localhost")
        mysql_database = getenv("HBNB_MYSQL_DB")

        # Create the database connection URI
        db_uri = f"""
        mysql+mysqldb://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_database}
        """

        # Create the engine with the URI and enable pool_pre_ping
        self.__engine = create_engine(db_uri, pool_pre_ping=True)
        # Drop all tables if environment is set to test
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects in the current database session"""
        objects = {}
        if cls:
            results = self.__session.query(cls).all()
            for obj in results:
                key = f"{self.__class__.__name__}.{obj.id}"
                objects[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                results = self.__session.query(cls).all()
                for obj in results:
                    key = f"{self.__class__.__name__}.{obj.id}"
                    objects[key] = obj

        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the db and create the current db session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
