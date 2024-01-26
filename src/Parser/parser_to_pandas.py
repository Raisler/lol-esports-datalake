# Build Parsers 
from datetime import datetime
import json
import pandas as pd

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
    return pd.DataFrame(game_time=game_time, game_id=game_id, **result)

def frame_parser_v2(frame, game_id):
    keys = {
        "totalGold": int,
        "level": int,
        "kills": int,
        "deaths": int,
        "assists": int,
        "creepScore": int,
        "currentHealth": int,
        "maxHealth": int
    }
    result = {}

    for p in frame['blueTeam']['participants'] + frame['redTeam']['participants']:
        particpant_id = f"participant{p['participantId']}_"
        for key in keys:
            result[f"{particpant_id}{key}"] = keys[key](p[key])
    
    
    keys_teams = {
            "totalGold": int, 
            "inhibitors": int, 
            "towers": int, 
            "barons": int, 
            "totalKills": int,
            "dragons": json.dumps
        }
    result_teams = {}
    
    for key in keys_teams:
        result_teams[f"blueTeam_{key}"] = keys_teams[key](frame["blueTeam"][key])
    
    for key in keys_teams:
        result_teams[f"redTeam_{key}"] = keys_teams[key](frame["redTeam"][key])
 
    
    game_time = frame['rfc460Timestamp']
    game_time = datetime.fromisoformat(game_time)
    
    return pd.DataFrame(dict(game_time=game_time, game_id=game_id, **result_teams, **result))
