from keys import API_URL_PERSISTED, KEY
import requests 
import json 

def leagues():
    leagues = requests.get(
        f"{API_URL_PERSISTED}/getLeagues?hl=pt-BR",
        headers = {'x-api-key': KEY}
        )
    
    return leagues.json()['data']['leagues']

def tournaments(tournament_id):
    tournaments = requests.get(
    f"{API_URL_PERSISTED}/getTournamentsForLeague",
    params = {'hl':'pt-BR', 'tournamentId': int(tournament_id)},
    headers = {'x-api-key': KEY}
)
    
    return tournaments
    