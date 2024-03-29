from src.Getter.live import get_all_frames_v2
from src.Getter.persisted import get_first_frame_time
from src.Parser.parser import frame_parser_v2
from src.model.s import Session
from src.Query.s import get_game_match_id
from src.Getter.persisted import getCompletedEvents
from src.Parser.parser import extract_all_matches, match_parser, game_parser
from src.Query import s as query
import pandas as pd

session = Session()

leagues = query.get_leagues()
leagues_df = pd.DataFrame([(l.name, l.region, l.league_id) for l in leagues],
                          columns = ['name', 'region', 'id'])

print(leagues_df)
league_choice = int(input("Choose a league by index: "))
league_id = int(leagues_df.loc[league_choice]['id'])

tournaments = query.get_tournaments(league_id)

tournaments_df = pd.DataFrame(
    [(t.slug, t.start_date, t.tournament_id) for t in tournaments],
    columns = ['slug', 'start_date', 'id'] 
)

print(tournaments_df)

tournament_choice = int(input("Choose a tournament by index: "))
tournament_id = int(tournaments_df.loc[tournament_choice]['id'])

matches = extract_all_matches(getCompletedEvents(tournament_id))
if len(query.get_matches_by_tournament_id(tournament_id)) < 1:
    for match in matches:
        data = match_parser(match, tournament_id)

        session.add(data)
        session.commit()
        
        for game_id in match['games_id']:
            game_id = int(game_id)
            data = game_parser(int(match['match_id']), game_id)
            session.add(data)
            session.commit()
else:
    pass 

failed_games_extract = [] 
frames_store = []
for m in matches:
    for game_id in m['games_id']:
        game_id = int(game_id)
        match_id = get_game_match_id(game_id)
        first_frame_time = get_first_frame_time(match_id, game_id) 
        if first_frame_time == None:
            print("first_frame_time null")
            failed_games_extract.append([m,game_id])
            continue
        else:
            frames = get_all_frames_v2(game_id, first_frame_time)
            for frame in frames:
                data = frame_parser_v2(frame, game_id)
                frames_store.append(data)
            
session.add_all(frames_store)
session.commit()
session.close()



