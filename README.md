# lol-esports-datalake
Get all information game, teams, tournaments and put on a datalake. Get Data from api lol-esports

Why a Relational Database?
Well, I do not care with ACID attribute of sql databases, but for my purpose sqlite3 is a good option, easy to modelling and make queries in future.

## Annotations

I didn't understand how to got the first frame, cause doesn't have the time of the game, just the utc time, so I will guide this by the gold of the game, if a team has 2500, means its the first minutes where anybody did not kill creeps.