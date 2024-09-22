from src.Getter.persisted import *
from src.Getter.live import *
from src.Parser.parser import *
from src.Parser.common import *


leagues = getLeagues()

for league in leagues.json()['data']['leagues']:
    print(league)