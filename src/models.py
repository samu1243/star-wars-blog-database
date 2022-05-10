import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from sqlalchemy import Enum

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'Planet'
    Planet_id = Column(Integer, primary_key=True)
    Planet_name = Column(String(250), nullable=False)
    Planet_diameter = Column(Integer, nullable=False)
    Planet_mass = Column(Integer, nullable=False)

class Character(Base):
    __tablename__ = 'Character'
    Character_id = Column(Integer, primary_key=True)
    Character_name = Column(String(50), nullable=False)
    Character_lastname = Column(String(50), nullable=False)
    Character_faction = Column(String(60), nullable=False)

class User(Base):
    __tablename__ = 'User'
    User_id = Column(Integer, primary_key=True)
    Username = Column(String(250), nullable=False)
    Firstname = Column(String(40), nullable=False)
    Lastname = Column(String(40), nullable=False)
    Email = Column(String(70), nullable=False)

class Favorite(Base):
    __tablename__ = 'Favorite'
    Favorite_id = Column(Integer, primary_key=True)
    Favorite_user_id = Column(Integer, ForeignKey('User.User_id'))
    Favorite_planet_id = Column(Integer, ForeignKey('Planet.Planet_id'))
    Favorite_character_id = Column(Integer, ForeignKey('Character.Character_id'))
    User = relationship(User)
    Planet = relationship(Planet)
    Character = relationship(Character)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')