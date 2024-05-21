import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)
    password = Column(String(32))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    mass = Column(Integer)
    color = Column(String(50))

class Favorites_Characters(Base):
    __tablename__ = 'favorites_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters_id_relationship = relationship(Characters)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    population = Column(Integer)
    climate = Column(String(50))
    gravity = Column(String(50))

class Favorites_Planets(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets_id_relatioship = relationship(Planets)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    passengers = Column(Integer)
    manufacturer = Column(String)
    crew = Column(Integer)

class Favorites_Starships(Base):
    __tablename__ = 'favorites_starships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)
    starships_id = Column(Integer, ForeignKey('starships.id'))
    starships_id_relationship = relationship(Starships)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
