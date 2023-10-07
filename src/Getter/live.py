from ..keys import API_URL_LIVE, KEY
import requests 
import json 
from datetime import datetime, timedelta
import time
from .handle_response import handle_response

def window_game(gameId, date):
    response = requests.get(
        f"{API_URL_LIVE}/window/{gameId}",
        params = { "hl": "pt-BR",
                "startingTime": date},
        headers = {'x-api-key': KEY},
    )
    return handle_response(response)


def get_game_details(match_id, date):
    response = requests.get(
        f"{API_URL_LIVE}/details/{match_id}",
        params = { "hl": "pt-BR",
                "startingTime": date},
        headers = {'x-api-key': KEY},
    )
    return handle_response(response)
    
    
# Esse aqui vai pegar um frame só    
def get_frame_window(gameId, date):
    response = requests.get(f"{API_URL_LIVE}/window/{gameId}",
        params = { "hl": "pt-BR",
                "startingTime": date},
        headers = {'x-api-key': KEY},
    )
    
    return handle_response(response)

def get_frames(gameId, date):
    response = requests.get(
        f"{API_URL_LIVE}/details/{gameId}",
        params = { "hl": "pt-BR",
                "startingTime": date},
        headers = {'x-api-key': KEY},
    )
    return response 

def add_date_seconds(date_string, seconds):
    input_datetime = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
    new_datetime = input_datetime + timedelta(seconds=seconds)
    return new_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')


def get_all_frames_window_game(gameId, firstFrameTime):
    store_frames = []
    initial_date = firstFrameTime
    last_date = 'start'
    while True:
        response = get_frames(gameId, initial_date)
        
        #if game_has_ended(store_frames):
            #break
        if response.status_code == 204:
            initial_date = add_date_seconds(initial_date, 60)  # Add 60 seconds
            print("Added 1 Minute")
        elif response.status_code == 200:
            for frame in response.json()['frames']:
                store_frames.append(frame)
            initial_date = add_date_seconds(initial_date, 20)  # Add 20 seconds
            print(last_date)
            if store_frames[-1]['rfc460Timestamp'] == last_date:
                break
            else:
                last_date = store_frames[-1]['rfc460Timestamp']
        else:
            print(response.status_code, response.content)  

        time.sleep(3)  # Wait for 1 second before the next attempt
        
    return store_frames