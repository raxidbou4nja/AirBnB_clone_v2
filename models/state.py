#!/usr/bin/python3
"""
Defines the State class.
"""

import models
from os import getenv
from models.base_model import Base, BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    Represents a state for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table states.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            cities = models.storage.all(City).values()
            filcities = [city for city in cities if city.state_id == self.id]
            return filcities

    @property
    def cities(self):
        """getters from storage linked to the current State"""
        city_obj = models.storage.all(City)
        return [city for city in city_obj.values() if city.state_id == self.id]
