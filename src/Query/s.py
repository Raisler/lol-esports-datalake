from ..model.s import Game, League, Session

session = Session()
def get_game_match_id(game_id):
    query = session.query(Game.game_id, Game.match_id).filter(Game.game_id == game_id)
    results = query.all()
    
    return results[0].match_id
