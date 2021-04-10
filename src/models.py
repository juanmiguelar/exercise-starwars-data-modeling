import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer, nullable=True)
    rotation_period = Column(Integer, nullable=True)
    orbital_period = Column(Integer, nullable=True)
    gravity = Column(Integer, nullable=True)
    population = Column(Integer, nullable=True)
    climate = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)
    surface_water = Column(Integer, nullable=True)
    created = Column(DateTime, nullable=True)
    edited = Column(DateTime, nullable=True)
    name = Column(String(250), nullable=True)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    height = Column(Integer, nullable=True)
    mass = Column(Integer, nullable=True)
    hair_color = Column(String(250), nullable=True)
    skin_color = Column(String(250), nullable=True)
    eye_color = Column(String(250), nullable=True)
    birth_year = Column(String(250), nullable=True)
    gender = Column(String(250), nullable=True)
    name = Column(String(250), nullable=True)
    created = Column(DateTime, nullable=True)
    edited = Column(DateTime, nullable=True)   

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    login = Column(String(250), nullable=True)
    passw = Column(String(250), nullable=True)

class Fav_Planet(Base):
    __tablename__ = 'fav_planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

class Fav_Character(Base):
    __tablename__ = 'fav_character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')