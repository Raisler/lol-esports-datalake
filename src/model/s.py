from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class League(Base):
    __tablename__ = 'leagues'

    id = Column(Integer, primary_key=True)
    slug = Column(String(40))
    name = Column(String(40))
    region = Column(String(40))

    tournaments = relationship('Tournament', back_populates='league')
    
class Tournament(Base):
    __tablename__ = 'tournaments'
    
    id = Column(Integer, primary_key=True)
    slug = Column(String(100))
    start_date = Column(Date)
    league_id = Column(Integer, ForeignKey('leagues.id'))  
    
    league = relationship('League', back_populates='tournaments')

class Strategy(Enum):
    BestOf1 = 'best_of_one'
    BestOf3 = 'best_of_three'
    BestOf5 = 'best_of_five'

class Games(Base):
    __tablename__ = 'games'

    match_id = Column(Integer, primary_key=True)
    strategy = Column(Enum(Strategy))
    team_0 = Column(String(25))
    team_1 = Column(String(25))
    startTime = Column(DateTime)
    
    league_id = Column(Integer, ForeignKey('leagues.id'))  
