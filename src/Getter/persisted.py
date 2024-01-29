import requests 
from .utils import handle_response
from dotenv import load_dotenv
import os 

load_dotenv() 
API_URL_PERSISTED = os.getenv("API_URL_PERSISTED")
KEY = os.getenv("KEY")


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


def get_event_details(match_id):
    response = requests.get(
    f"{API_URL_PERSISTED}/getEventDetails",
    params = {'hl':'pt-BR', 'id': match_id},
    headers = {'x-api-key': KEY}
)
    
    return handle_response(response)

def get_first_frame_time(match_id, game_id):
    data = get_event_details(match_id)
    for game in data.json()['data']['event']['match']['games']:
        first_frame_time = game['vods'][0]['firstFrameTime']
        game_id_to_compare = int(game['id'])
        if game_id_to_compare == game_id:
            return first_frame_time 
        else:    
            continue
        
def get_live_game():
    response = requests.get(f"{API_URL_PERSISTED}/getLive/",
        params = { "hl": "pt-BR"},
        headers = {'x-api-key': KEY},
    )
    
    return handle_response(response)