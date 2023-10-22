from src.Getter.persisted import *
from src.Getter.live import *
from src.Parser.parser import *
from src.Parser.common import *
from src.model.s import Session

session = Session()

leagues = getLeagues()

for league in leagues.json()['data']['leagues']:
    data = league_parser(league)

    session.add(data)
    session.commit()

session.close()