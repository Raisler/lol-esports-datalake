# Build Parsers 
import json 

def frames_parser(frames):
    result = []
    keys = [
        "participantId",
        "level",
        "kills",
        "deaths",
        "assists",
        "totalGoldEarned",
        "creepScore",
        "killParticipation",
        "championDamageShare",
        "wardsPlaced",
        "wardsDestroyed",
        "attackDamage",
        "abilityPower",
        "criticalChance",
        "attackSpeed",
        "lifeSteal",
        "armor",
        "magicResistance",
        "tenacity",
        "items",
        "perkMetadata"
    ]

    for frame in frames:
        for p in frame['participants']:
            # Use a list comprehension to extract values using shorthand notation
            extracted_values = [p[key] for key in keys]
            result.append(extracted_values)

    return result


def extract_match_info(data):
    match_info = []

    # Extract match information from each event
    for event in data['data']['schedule']['events']:
        match_id = event["match"]["id"]
        name_team0 = event['match']['teams'][0]['name']
        name_team1 = event['match']['teams'][1]['name']
        result_team0 = event.get("match", {}).get("teams", [{}])[0].get("result", {}).get("gameWins")
        result_team1 = event.get("match", {}).get("teams", [{}])[1].get("result", {}).get("gameWins")
        strategy_type = event.get("match", {}).get("strategy", {}).get("type")
        strategy_count = event.get("match", {}).get("strategy", {}).get("count")
        match_info.append({
            "match_id": match_id,
            "name_team0": name_team0,
            "name_team1": name_team1,
            "result_team0": result_team0,
            "result_team1": result_team1,
            "strategy": strategy_type + str(strategy_count),
            "games_id": [game_id['id'] for game_id in event['games'] if len(game_id.get('vods', [])) != 0]
        })
        
        

    return match_info