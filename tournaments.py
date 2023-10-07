from src.Getter.persisted import getTournaments
from src.Parser.common import tournament_parser
from src.model.s import Session

session = Session()
league_id = 98767991332355509
tournaments = getTournaments(league_id)

for t in tournaments.json()['data']['leagues'][0]['tournaments']:
    data = tournament_parser(t, league_id)

    session.add(data)
    session.commit()

session.close()


#cblol_2023_2 = getCompletedEvents(110413046183015975) # Tournament ID
#frames = get_all_frames_window_game(110471059652887237, '2023-08-19T16:11:20Z')
# Now I need to fullfill my db with tournaments

