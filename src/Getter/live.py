from ..keys import API_URL_LIVE, KEY
import requests 
import json 
from datetime import datetime, timedelta
import time
from .utils import handle_response, is_internet_available

def make_divisible_by_10(date_string):
    # Convert the date string to a datetime object
    dt = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')

    # Calculate the remainder when dividing the seconds by 10
    remainder = dt.second % 10

    # If it's not already divisible by 10, calculate the number of seconds to add
    if remainder != 0:
        seconds_to_add = 10 - remainder
        dt += timedelta(seconds=seconds_to_add)

    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')


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
    return handle_response(response)

def add_date_seconds(date_string, seconds):
    input_datetime = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
    new_datetime = input_datetime + timedelta(seconds=seconds)
    return new_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')


def get_all_frames_window_game(gameId, firstFrameTime):
    store_frames = []
    initial_date = make_divisible_by_10(firstFrameTime)
    last_date = 'start'
    while True:
        if is_internet_available():
            response = get_frames(gameId, initial_date)
            
            if response.status_code != 204:
                time.sleep(120)
            if response.status_code == 204:
                initial_date = add_date_seconds(initial_date, 60)  # Add 60 seconds
                print("Added 1 Minute")
            elif response.status_code == 200:
                for frame in response.json()['frames']:
                    store_frames.append(frame)
                initial_date = add_date_seconds(initial_date, 20)  # Add 15 seconds
                print(last_date)
                if store_frames[-1]['rfc460Timestamp'] == last_date:
                    break
                else:
                    last_date = store_frames[-1]['rfc460Timestamp']
            else:
                print(response.status_code, response.content)  

            time.sleep(20) 
        else:
            time.sleep(30)
        
    return store_frames