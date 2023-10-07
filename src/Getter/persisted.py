import requests 
from .handle_response import handle_response
from ..keys import API_URL_PERSISTED, KEY


def getLeagues():
    leagues = requests.get(
        f"{API_URL_PERSISTED}/getLeagues?hl=pt-BR",
        headers = {'x-api-key': KEY}
        )
    
    return handle_response(leagues)

def getTournaments(tournament_id):
    tournaments = requests.get(
    f"{API_URL_PERSISTED}/getTournamentsForLeague",
    params = {'hl':'pt-BR', 'leagueId': int(tournament_id)},
    headers = {'x-api-key': KEY}
)
    
    return handle_response(tournaments)
    
    
def getCompletedEvents(tournament_id):
    tournament_data = requests.get(
    f"{API_URL_PERSISTED}/getCompletedEvents",
    params = {'hl':'pt-BR', 'tournamentId':[tournament_id]},
    headers = {'x-api-key': KEY}
)
    
    return handle_response(tournament_data)





