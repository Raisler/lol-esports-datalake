import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import datetime as datetime

db_url = 'sqlite:///datalake.sqlite'
engine = create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# CBLOL ID
tournament_id = 110413046183015975

sql_query = text(
    """
    SELECT matches.*, frames_two.*
    FROM frames_two
    JOIN games ON frames_two.game_id = games.game_id
    JOIN matches ON games.match_id = matches.match_id
    WHERE matches.tournament_id = :tournament_id
    """
)

connection = session.connection()
result = connection.execute(sql_query, {"tournament_id": tournament_id})
df = pd.DataFrame(result.fetchall(), columns=result.keys())


def who_won(row):
    if row['result_team0'] == 1 and row['result_team1'] == 0:
        return 0
    if row['result_team0'] == 0 and row['result_team1'] == 1:
        return 1
    else:
        return 3
    
df['target'] = df.apply(who_won, axis=1)
df = df[df['target'].isin([0, 1])]
df['time'] = pd.to_datetime(df['game_time'])
df['time_'] =  df.groupby('game_id')['time'].apply(lambda x: (x - x.iloc[0])).reset_index(drop=True).dt.total_seconds()
#df = df.query('300 <= time_ <= 1160')

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import Normalizer
from sklearn.ensemble import RandomForestClassifier

features_columns = ['blueTeam_totalGold', 'blueTeam_inhibitors',
       'blueTeam_towers', 'blueTeam_barons', 'blueTeam_totalKills',
 'redTeam_totalGold', 'redTeam_inhibitors',
       'redTeam_towers', 'redTeam_barons', 'redTeam_totalKills',
 'participant1_totalGold', 'participant1_level',
       'participant1_kills', 'participant1_deaths', 'participant1_assists',
       'participant1_creepScore', 'participant1_currentHealth',
       'participant1_maxHealth', 'participant2_totalGold',
       'participant2_level', 'participant2_kills', 'participant2_deaths',
       'participant2_assists', 'participant2_creepScore',
       'participant2_currentHealth', 'participant2_maxHealth',
       'participant3_totalGold', 'participant3_level', 'participant3_kills',
       'participant3_deaths', 'participant3_assists',
       'participant3_creepScore', 'participant3_currentHealth',
       'participant3_maxHealth', 'participant4_totalGold',
       'participant4_level', 'participant4_kills', 'participant4_deaths',
       'participant4_assists', 'participant4_creepScore',
       'participant4_currentHealth', 'participant4_maxHealth',
       'participant5_totalGold', 'participant5_level', 'participant5_kills',
       'participant5_deaths', 'participant5_assists',
       'participant5_creepScore', 'participant5_currentHealth',
       'participant5_maxHealth', 'participant6_totalGold',
       'participant6_level', 'participant6_kills', 'participant6_deaths',
       'participant6_assists', 'participant6_creepScore',
       'participant6_currentHealth', 'participant6_maxHealth',
       'participant7_totalGold', 'participant7_level', 'participant7_kills',
       'participant7_deaths', 'participant7_assists',
       'participant7_creepScore', 'participant7_currentHealth',
       'participant7_maxHealth', 'participant8_totalGold',
       'participant8_level', 'participant8_kills', 'participant8_deaths',
       'participant8_assists', 'participant8_creepScore',
       'participant8_currentHealth', 'participant8_maxHealth',
       'participant9_totalGold', 'participant9_level', 'participant9_kills',
       'participant9_deaths', 'participant9_assists',
       'participant9_creepScore', 'participant9_currentHealth',
       'participant9_maxHealth', 'participant10_totalGold',
       'participant10_level', 'participant10_kills', 'participant10_deaths',
       'participant10_assists', 'participant10_creepScore',
       'participant10_currentHealth', 'participant10_maxHealth', 'time_']

features = df[features_columns]
target = df['target']

X_train, X_test, y_train, y_test = train_test_split(
     features, target, test_size=0.09, random_state=42)


transformer = Normalizer().fit(X_train) 
X_train = transformer.transform(X_train)
X_test = transformer.transform(X_test)

clf = RandomForestClassifier(max_depth=18, random_state=0)
model = clf.fit(X_train, y_train)
y_pred = model.predict(X_test)

target_names = ['BLUE', 'RED']
print(classification_report(y_test, y_pred, target_names=target_names))