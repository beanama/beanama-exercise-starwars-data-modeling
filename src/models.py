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
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    planet = Column(String(250), nullable=False)


class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)

    
class Film(Base):
    __tablename__ = 'film'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    director = Column(String(255), nullable=False)
    year_released = Column(String(255), nullable=False)
    author = relationship(User)
    character = relationship(Character)


class Favourite(Base):
    __tablename__ = 'favourite'

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    film_id = Column(Integer, ForeignKey('film.id'))

    #Relationships
    user = relationship(User, backref='favourites')
    planet = relationship(Planet)
    character = relationship(Character)
    film = relationship(Film)

    def to_dict(self):
        return {}
 
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
