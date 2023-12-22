#!/usr/bin/python3
"""Defines the DBStorage engine."""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Represents a database storage engine."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        db_config = {
            "user": getenv("HBNB_MYSQL_USER"),
            "passwd": getenv("HBNB_MYSQL_PWD"),
            "host": getenv("HBNB_MYSQL_HOST"),
            "db": getenv("HBNB_MYSQL_DB"),
        }
        self.__engine = create_engine(
            "mysql+mysqldb://{user}:{passwd}@{host}/{db}".
            format(user=getenv("HBNB_MYSQL_USER"),
                   passwd=getenv("HBNB_MYSQL_PWD"),
                   host=getenv("HBNB_MYSQL_HOST"),
                   db=getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True
        )

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database all objects of the given class."""
        classes = [State, City, User, Place, Review, Amenity]

        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            classes = [cls]

        objs = [obj for cls in classes
                for obj in self.__session.query(cls).all()]
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        ses_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()
