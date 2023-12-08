import pickle 
from src.Getter.persisted import get_first_frame_time
from src.Query.s import get_game_match_id
from src.Parser.parser import frame_parser
from src.Getter.live import get_all_frames_window_game
from src.model.s import Session
session = Session()
import time 

start_time = time.time()

game_id = 107405837336900396 #FLA VS FUR
match_id = get_game_match_id(game_id)
first_frame_time = get_first_frame_time(match_id, game_id) 
frames = get_all_frames_window_game(game_id, first_frame_time)

end_time = time.time()


elapsed_time = end_time - start_time

print(f"The function to get the frames took {elapsed_time:.2f} seconds to execute.")

start_time = time.time()

frames_store = []
for frame in frames:
    data = frame_parser(frame, game_id)
    frames_store.append(data)
    
end_time = time.time()

print(f"The function to store the frames took {elapsed_time:.2f} seconds to execute.")


'''
for frame in frames:
    data = frame_parser(frame, game_id)
    
    session.add(data)
    session.commit()
    
session.close()
'''