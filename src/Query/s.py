from ..model.s import Game, League, Session, Tournament, Match

session = Session()
def get_game_match_id(game_id):
    query = session.query(Game.game_id, Game.match_id).filter(Game.game_id == game_id)
    results = query.all()
    
    return results[0].match_ids

def get_leagues():
    query = session.query(League)
    results = query.all()
    
    return results

def get_tournaments(league_id):
    query = session.query(Tournament).filter(Tournament.league_id == league_id)
    results = query.all()
    
    return results 


def get_all_games_by_tournament(tournament_id):
    query = session.query(Game.game_id, Game.match_id).filter(Game.game_id == game_id)
    pass


def get_matches_by_tournament_id(tournament_id):
    query = session.query(Match).filter(Match.tournament_id == tournament_id)
    results = query.all()
    
    return results