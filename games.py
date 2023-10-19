from src.Getter.persisted import getCompletedEvents
from src.Parser.parser import extract_all_matches, game_parser
from src.model.s import Session

session = Session()
tournament_id = 107405837336179496 #cblol 2022.1

matches = extract_all_matches(getCompletedEvents(tournament_id))
matches = (matches)


for match in matches:
    for game_id in match['games_id']:
            data = game_parser(match['match_id'], game_id)
            session.add(data)
            session.commit()

session.close()