#!/usr/bin/python3
"""
Defines the City class.
"""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    Represents a city for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table cities.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="city", cascade="delete")
