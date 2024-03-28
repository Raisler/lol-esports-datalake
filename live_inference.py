from src.Getter.persisted import get_live_game
from src.Query import s as query
from src.model.s import Session
import pandas as pd
from src.Getter.live import window_game, get_frames
from datetime import datetime
from src.Parser.parser_to_pandas import frame_parser,frame_parser_v2
session = Session()

leagues = query.get_leagues()
leagues_df = pd.DataFrame([(l.name, l.region, l.league_id) for l in leagues],
                          columns = ['name', 'region', 'id'])
print(leagues_df)
league_choice = int(input("Choose a league by index: "))
league_id = int(leagues_df.loc[league_choice]['id'])


r = get_live_game()

data = None
for i in r.json()['data']['schedule']['events']:
    if int(i['league']['id']) == league_id:
        data = i
       

from datetime import datetime, timedelta
def make_divisible_by_10(date_string):
    # Convert the date string to a datetime object
    dt = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')

    # Subtract the remainder when dividing the seconds by  10
    remainder = dt.second %  10
    seconds_to_subtract = remainder
    dt -= timedelta(seconds=seconds_to_subtract)

    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')


now =  datetime.utcnow()

# Format the date and time to the required format
date = make_divisible_by_10(now.strftime('%Y-%m-%dT%H:%M:%SZ'))
game_id = int(data['match']['games'][0]['id'])

# frame_game = window_game(game_id, date)
# df = frame_parser_v2(frame_game, game_id)

frame_game = get_frames(game_id, date)
df = frame_parser(frame_game, game_id)