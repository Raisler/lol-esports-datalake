from src.Getter.live import get_all_frames_window_game
from src.Getter.persisted import get_first_frame_time
from src.Parser.parser import frame_parser
from src.model.s import Session
from src.Query.s import get_game_match_id
from src.Getter.persisted import getCompletedEvents, getTournaments
from src.Parser.parser import extract_all_matches, match_parser
from src.Parser.common import tournament_parser
from src.Query import s as query
import time
import pandas as pd
session = Session()


leagues = query.get_leagues()
leagues_df = pd.DataFrame([(l.name, l.region, l.league_id) for l in leagues],
                          columns = ['name', 'region', 'id'])

print(leagues_df)
league_choice = int(input("Choose a league by index: "))
league_id = int(leagues_df.loc[league_choice]['id'])

tournaments = query.get_tournaments(league_id)

if len(tournaments) < 1:
    tournaments = getTournaments(league_id)

    for t in tournaments.json()['data']['leagues'][0]['tournaments']:
        data = tournament_parser(t, league_id)

        session.add(data)
        session.commit()
else:
    pass

tournaments = query.get_tournaments(league_id)
tournaments_df = pd.DataFrame(
    [(t.slug, t.start_date, t.tournament_id) for t in tournaments],
    columns = ['slug', 'start_date', 'id'] 
)

print(tournaments_df)

# After Tournament I Need to take all matches from that
# Check if the matches exist in tournament, make later

tournament_choice = int(input("Choose a tournament by index: "))
tournament_id = int(tournaments_df.loc[tournament_choice]['id'])

matches = query.get_matches_by_tournament_id(tournament_id)


if len(matches) < 1:
    matches = extract_all_matches(getCompletedEvents(tournament_id))

    for match in matches:
        data = match_parser(match, tournament_id)

        session.add(data)
        session.commit()
else:
    pass 

for m in matches:
    for game_id in m['games_id']:
        match_id = get_game_match_id(game_id)
        first_frame_time = get_first_frame_time(match_id, game_id) 

        frames = get_all_frames_window_game(game_id, first_frame_time)
        for frame in frames:
            data = frame_parser(frame, game_id)
            
            session.add(data)
            session.commit()
    
#end
#session.close()
