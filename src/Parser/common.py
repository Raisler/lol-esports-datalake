from ..model.s import League, Tournament
from datetime import datetime


def league_parser(data):
    league_id = data['id']
    slug = data['slug']
    name = data['name']
    region = data['region']
    
    return League(league_id=int(league_id), slug=slug,name=name, region=region)
    

def tournament_parser(data, league_id):
    tournament_id = data['id']
    slug = data['slug']
    startDate = data['startDate']
    date_obj = datetime.strptime(startDate, '%Y-%m-%d').date()
    
    return Tournament(tournament_id=int(tournament_id), slug=slug, start_date=date_obj, league_id=league_id)
  
