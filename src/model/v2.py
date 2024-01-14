from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum, Date, Float, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

db_url = 'sqlite:///datalake_2.sqlite'
engine = create_engine(db_url, echo=True)

Base = declarative_base()

class League(Base):
    __tablename__ = 'leagues'

    league_id = Column(Integer, primary_key=True, autoincrement=False)
    slug = Column(String(100))
    name = Column(String(100))
    region = Column(String(100))

    tournaments = relationship('Tournament', back_populates='league')
    
class Tournament(Base):
    __tablename__ = 'tournaments'
    
    tournament_id = Column(Integer, primary_key=True, autoincrement=False)
    slug = Column(String(100))
    start_date = Column(Date)
    league_id = Column(Integer, ForeignKey('leagues.league_id'))  
    
    league = relationship('League', back_populates='tournaments')
    
class Match(Base):
    __tablename__ = 'matches'
    
    match_id = Column(Integer, primary_key=True, autoincrement=False)
    start_time = Column(DateTime)
    tournament_id = Column(Integer, ForeignKey('tournaments.tournament_id'))  # Corrected this line
    strategy = Column(String)    
    name_team0 = Column(String)
    name_team1 = Column(String)
    result_team0 = Column(Integer)
    result_team1 = Column(Integer)
    
    # One-to-many relationship: Match can have multiple Games
    games = relationship("Game", back_populates="match")

class Game(Base): 
    __tablename__ = 'games'

    game_id = Column(Integer, primary_key=True, autoincrement=False)
    
    match_id = Column(Integer, ForeignKey('matches.match_id'))
    frames = relationship("Frame", back_populates="game")
    match = relationship("Match", back_populates="games")
    
    

class Frame(Base):
    __tablename__ = 'frames'
    
    id = Column(Integer, primary_key=True)
    game_time = Column(DateTime)
    
    # Many-to-one relationship: Frame belongs to one Game
    game_id = Column(Integer, ForeignKey('games.game_id'))
    
    # Define a back reference to access the parent Game from Frame
    game = relationship("Game", back_populates="frames")    
    
    blueTeam_totalGold = Column(Integer)
    blueTeam_inhibitors = Column(Integer)
    blueTeam_towers = Column(Integer)
    blueTeam_barons = Column(Integer)
    blueTeam_totalKills = Column(Integer)
    blueTeam_dragons = Column(JSON)  
     
    redTeam_totalGold = Column(Integer)
    redTeam_inhibitors = Column(Integer)
    redTeam_towers = Column(Integer)
    redTeam_barons = Column(Integer)
    redTeam_totalKills = Column(Integer)
    redTeam_dragons = Column(JSON)
    
    participant1_totalGold = Column(Integer)
    participant1_level = Column(Integer)
    participant1_kills = Column(Integer)
    participant1_deaths = Column(Integer)
    participant1_assists  = Column(Integer)
    participant1_creepScore  = Column(Integer)
    participant1_currentHealth = Column(Integer)
    participant1_maxHealth  = Column(Integer)
    
    participant2_totalGold = Column(Integer)
    participant2_level = Column(Integer)
    participant2_kills = Column(Integer)
    participant2_deaths = Column(Integer)
    participant2_assists  = Column(Integer)
    participant2_creepScore  = Column(Integer)
    participant2_currentHealth = Column(Integer)
    participant2_maxHealth  = Column(Integer)
    
    participant3_totalGold = Column(Integer)
    participant3_level = Column(Integer)
    participant3_kills = Column(Integer)
    participant3_deaths = Column(Integer)
    participant3_assists  = Column(Integer)
    participant3_creepScore  = Column(Integer)
    participant3_currentHealth = Column(Integer)
    participant3_maxHealth  = Column(Integer)
    
    participant4_totalGold = Column(Integer)
    participant4_level = Column(Integer)
    participant4_kills = Column(Integer)
    participant4_deaths = Column(Integer)
    participant4_assists  = Column(Integer)
    participant4_creepScore  = Column(Integer)
    participant4_currentHealth = Column(Integer)
    participant4_maxHealth  = Column(Integer)
    
    participant5_totalGold = Column(Integer)
    participant5_level = Column(Integer)
    participant5_kills = Column(Integer)
    participant5_deaths = Column(Integer)
    participant5_assists  = Column(Integer)
    participant5_creepScore  = Column(Integer)
    participant5_currentHealth = Column(Integer)
    participant5_maxHealth  = Column(Integer)
    
    participant6_totalGold = Column(Integer)
    participant6_level = Column(Integer)
    participant6_kills = Column(Integer)
    participant6_deaths = Column(Integer)
    participant6_assists  = Column(Integer)
    participant6_creepScore  = Column(Integer)
    participant6_currentHealth = Column(Integer)
    participant6_maxHealth  = Column(Integer)
    
    participant7_totalGold = Column(Integer)
    participant7_level = Column(Integer)
    participant7_kills = Column(Integer)
    participant7_deaths = Column(Integer)
    participant7_assists  = Column(Integer)
    participant7_creepScore  = Column(Integer)
    participant7_currentHealth = Column(Integer)
    participant7_maxHealth  = Column(Integer)
    
    participant8_totalGold = Column(Integer)
    participant8_level = Column(Integer)
    participant8_kills = Column(Integer)
    participant8_deaths = Column(Integer)
    participant8_assists  = Column(Integer)
    participant8_creepScore  = Column(Integer)
    participant8_currentHealth = Column(Integer)
    participant8_maxHealth  = Column(Integer)
    
    participant9_totalGold = Column(Integer)
    participant9_level = Column(Integer)
    participant9_kills = Column(Integer)
    participant9_deaths = Column(Integer)
    participant9_assists  = Column(Integer)
    participant9_creepScore  = Column(Integer)
    participant9_currentHealth = Column(Integer)
    participant9_maxHealth  = Column(Integer)
    
    participant10_totalGold = Column(Integer)
    participant10_level = Column(Integer)
    participant10_kills = Column(Integer)
    participant10_deaths = Column(Integer)
    participant10_assists  = Column(Integer)
    participant10_creepScore  = Column(Integer)
    participant10_currentHealth = Column(Integer)
    participant10_maxHealth  = Column(Integer)

    
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)