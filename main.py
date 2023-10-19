from src.Getter.live import get_all_frames_window_game
from src.Getter.persisted import get_first_frame_time
from src.Parser.parser import frame_parser
from src.model.s import Session
from src.Query.s import get_game_match_id
import time
session = Session()

game_id = 107405837336900396
match_id = get_game_match_id(game_id)
first_frame_time = get_first_frame_time(match_id, game_id)  # I have to take the first_frame, getEventDetails, but I need to take the match


time.sleep(20)
frames = get_all_frames_window_game(game_id, first_frame_time)
for frame in frames:
    data = frame_parser(frame, game_id)
    
    session.add(data)
    session.commit()
    
session.close()