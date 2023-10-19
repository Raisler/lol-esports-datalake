from src.Getter.persisted import getCompletedEvents
from src.Parser.parser import extract_all_matches, match_parser
from src.model.s import Session

session = Session()
tournament_id = 107405837336179496 #cblol 2022.1

matches = extract_all_matches(getCompletedEvents(tournament_id))
matches = (matches)


for match in matches:
    data = match_parser(match, tournament_id)

    session.add(data)
    session.commit()

session.close()
