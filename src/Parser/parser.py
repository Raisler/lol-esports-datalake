# Build Parsers 
from ..model.s import Match, Game, Strategy, Frame
from datetime import datetime
import json


# def frame_parser(frame, game_id):
#     result = []
#     keys = {
#         "level": int,
#         "kills": int,
#         "deaths": int,
#         "assists": int,
#         "totalGoldEarned": int,
#         "creepScore": int,
#         "killParticipation":float,
#         "championDamageShare":float,
#         "wardsPlaced": int,
#         "wardsDestroyed": int,
#         "attackDamage": int,
#         "abilityPower": int,
#         "criticalChance":float,
#         "attackSpeed": int,
#         "lifeSteal":float,
#         "armor": int,
#         "magicResistance": int,
#         "tenacity":float,
#         "items":json.dumps,
#         "perkMetadata": json.dumps
#     }

#     #for frame in frames:
#     for p in frame['participants']:
#         extracted_values = [keys[key](p[key]) for key in keys]
#         result.extend(extracted_values)
        
#     game_time = frame['rfc460Timestamp']
#     game_time = datetime.fromisoformat(game_time)
    
#     #return result
#     return Frame(game_time = game_time, game_id = game_id, *result)  
def frame_parser(frame, game_id):
    keys = {
        "level": int,
        "kills": int,
        "deaths": int,
        "assists": int,
        "totalGoldEarned": int,
        "creepScore": int,
        "killParticipation": float,
        "championDamageShare": float,
        "wardsPlaced": int,
        "wardsDestroyed": int,
        "attackDamage": int,
        "abilityPower": int,
        "criticalChance": float,
        "attackSpeed": int,
        "lifeSteal": float,
        "armor": int,
        "magicResistance": int,
        "tenacity": float,
        "items": json.dumps,
        "perkMetadata": json.dumps
    }

    result = {}

    for p in frame['participants']:
        particpant_id = f"participant{p['participantId']}_"
        for key in keys:
            result[f"{particpant_id}{key}"] = keys[key](p[key])
    
    game_time = frame['rfc460Timestamp']
    game_time = datetime.fromisoformat(game_time)
    
    # Use dictionary unpacking to pass the extracted values as keyword arguments
    return Frame(game_time=game_time, game_id=game_id, **result)

def extract_all_matches(data):
    match_info = []

    # Extract match information from each event
    for event in data.json()['data']['schedule']['events']:
        match_id = event["match"]["id"]
        start_time = event["startTime"]
        start_time = datetime.fromisoformat(start_time)
        name_team0 = event['match']['teams'][0]['name']
        name_team1 = event['match']['teams'][1]['name']
        result_team0 = event.get("match", {}).get("teams", [{}])[0].get("result", {}).get("gameWins")
        result_team1 = event.get("match", {}).get("teams", [{}])[1].get("result", {}).get("gameWins")
        strategy_type = event.get("match", {}).get("strategy", {}).get("type")
        strategy_count = event.get("match", {}).get("strategy", {}).get("count")
        match_info.append({
            "match_id": match_id,
            "start_time": start_time,
            "name_team0": name_team0,
            "name_team1": name_team1,
            "result_team0": result_team0,
            "result_team1": result_team1,
            "strategy": strategy_type + str(strategy_count),
            "games_id": [game_id['id'] for game_id in event['games'] if len(game_id.get('vods', [])) != 0]
        })
        
        
        
    return match_info


# Colocar Tournament id em extract_match_info ou em match_parser?
# Take winner when?
    
def match_parser(data, tournament_id):
    strategies = {'bestOf1': Strategy.BestOf1, 
                'bestOf3': Strategy.BestOf3,
                'bestOf5': Strategy.BestOf5}
        
    return Match(match_id=data['match_id'], start_time=data['start_time'],
                 tournament_id = tournament_id, 
                 strategy=strategies.get(data['strategy']),
                 name_team0=data['name_team0'], name_team1=data['name_team1'],
                 result_team0=data['result_team0'], result_team1=data['result_team1'])
    
def game_parser(match_id,game_id):
    return Game(game_id=game_id, match_id=match_id)
