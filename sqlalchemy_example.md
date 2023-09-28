Just to remember how to use SQLALchemy


```python: 
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Replace 'your_database_name.db' with the desired database name
db_url = 'sqlite:///your_database_name.db'
engine = create_engine(db_url, echo=True)  # Set echo=True for debugging

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"
    
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='John Doe', age=30)
session.add(new_user)
session.commit()

session.close()

```


First Json file:
```json 
{
  "esportsGameId": "string",
  "esportsMatchId": "string",
  "gameMetadata": {
    "patchVersion": "string",
    "blueTeamMetadata": {
      "esportsTeamId": "string",
      "participantMetadata": [
        {
          "participantId": 1,
          "summonerName": "string",
          "championId": "string",
          "role": "top"
        }
      ]
    },
    "redTeamMetadata": {
      "esportsTeamId": "string",
      "participantMetadata": [
        {
          "participantId": 1,
          "summonerName": "string",
          "championId": "string",
          "role": "top"
        }
      ]
    }
  },
  "frames": [
    {
      "rfc460Timestamp": "2023-08-22T14:14:09Z",
      "gameState": "in_game",
      "blueTeam": {
        "totalGold": 0,
        "inhibitors": 0,
        "towers": 0,
        "barons": 0,
        "totalKills": 0,
        "dragons": [
          "ocean"
        ],
        "participants": [
          {
            "participantId": 1,
            "level": 0,
            "kills": 0,
            "deaths": 0,
            "assists": 0,
            "creepScore": 0,
            "totalGold": 0,
            "currentHealth": 0,
            "maxHealth": 0
          }
        ]
      },
      "redTeam": {
        "totalGold": 0,
        "inhibitors": 0,
        "towers": 0,
        "barons": 0,
        "totalKills": 0,
        "dragons": [
          "ocean"
        ],
        "participants": [
          {
            "participantId": 1,
            "level": 0,
            "kills": 0,
            "deaths": 0,
            "assists": 0,
            "creepScore": 0,
            "totalGold": 0,
            "currentHealth": 0,
            "maxHealth": 0
          }
        ]
      }
    }
  ]
}
```


Second Json:
```json
{
  "frames": [
    {
      "rfc460Timestamp": "2023-08-22T14:14:09Z",
      "participants": [
        {
          "participantId": 1,
          "level": 0,
          "kills": 0,
          "deaths": 0,
          "assists": 0,
          "creepScore": 0,
          "totalGold": 0,
          "currentHealth": 0,
          "maxHealth": 0,
          "totalGoldEarned": 0,
          "killParticipation": 0,
          "championDamageShare": 0,
          "wardsPlaced": 0,
          "wardsDestroyed": 0,
          "attackDamage": 0,
          "abilityPower": 0,
          "criticalChance": 0,
          "attackSpeed": 0,
          "lifeSteal": 0,
          "armor": 0,
          "magicResistance": 0,
          "tenacity": 0,
          "items": [
            0
          ],
          "perkMetadata": {
            "styleId": 8000,
            "subStyleId": 8000,
            "perks": [
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ]
          },
          "abilities": "Q"
        }
      ]
    }
  ]
}
```

Based on this two Json files, I need to modelling a database (datalake) in python SQLAlchemy, follow the example:

```python
class League(Base):
    __tablename__ = 'leagues'

    id = Column(Integer, primary_key=True)
    slug = Column(String(40))
    name = Column(String(40))
    region = Column(String(40))

    tournaments = relationship('Tournament', back_populates='league')
```
