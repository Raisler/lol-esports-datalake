import pickle 
from src.Getter.persisted import get_first_frame_time
from src.Query.s import get_game_match_id
from src.Parser.parser import frame_parser
from src.model.s import Session
session = Session()

with open("frames", "rb") as fp: 
    frames = pickle.load(fp)
    
game_id = 107405837336900396
match_id = get_game_match_id(game_id)
first_frame_time = get_first_frame_time(match_id, game_id) 

for frame in frames:
    data = frame_parser(frame, game_id)
    
    session.add(data)
    session.commit()
    
session.close()