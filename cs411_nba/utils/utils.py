from nba_api.stats.static import players
player_dict = players.get_players()
# from https://www.playingnumbers.com/2019/12/how-to-get-nba-data-using-the-nba_api-python-module-beginner/
# Use ternary operator or write function
# Names are case sensitive
#example to find lebron
bron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
bron_id = bron['id']

# find team Ids
from nba_api.stats.static import teams
teams = teams.get_teams()
#example to find GSW team
GSW = [x for x in teams if x['full_name'] == 'Golden State Warriors'][0]
GSW_id = GSW['id']

#better example below from https://medium.com/better-programming/using-pythons-nba-api-to-create-a-simple-regression-model-ac9a3b36bc8
import pandas as pd
import numpy as np
import requests
from nba_api.stats import endpoints
data = endpoints.leagueleaders.LeagueLeaders()# Here we access the leagueleaders module through endpoints & assign the class to "data"


# Our "data" variable now has built in functions such as creating a dataframe for our data
df = data.league_leaders.get_data_frame()
df.head()
