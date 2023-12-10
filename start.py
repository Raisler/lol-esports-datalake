# Here I will put to start the database with all leagues, tournaments, etc

import subprocess

# Make user input to choose the Tournament or add all Tournaments :D 

# Leagues
subprocess.run(["python leagues.py"], shell=True, capture_output=True, text=True)

# Tournaments
subprocess.run(["python tournaments.py"], shell=True, capture_output=True, text=True)

# Matches