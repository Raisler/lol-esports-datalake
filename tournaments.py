from src.Getter.persisted import getTournaments
from src.Parser.common import tournament_parser
from src.model.s import Session
import pandas as pd
from src.Query.s import query 
session = Session()


leagues = query.get_leagues()
leagues_df = pd.DataFrame([(l.name, l.region, l.league_id) for l in leagues],
                          columns = ['name', 'region', 'id'])

print(leagues_df)
league_choice = int(input("Choose a league by index: "))
league_id = int(leagues_df.loc[league_choice]['id'])


tournaments = getTournaments(league_id)

for t in tournaments.json()['data']['leagues'][0]['tournaments']:
    data = tournament_parser(t, league_id)

    session.add(data)
    session.commit()

session.close()


