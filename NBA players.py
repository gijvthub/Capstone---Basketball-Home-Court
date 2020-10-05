from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
import pandas as pd
player_list = players.get_players()
playerdatalist = pd.DataFrame(player_list)
#x= '2544'
ids = (playerdatalist['id'])
len(ids)

gamelogs = playergamelog.PlayerGameLog(player_id = '1629630',season = '2019')
gamelogs_df1 = gamelogs.get_data_frames()[0]
gamelogs = playergamelog.PlayerGameLog(player_id = '203506',season = '2019')
gamelogs_df2 = gamelogs.get_data_frames()[0]
gamelogs = playergamelog.PlayerGameLog(player_id = '1626162',season = '2019')
gamelogs_df3 = gamelogs.get_data_frames()[0]
gamelogs = playergamelog.PlayerGameLog(player_id = '201937',season = '2019')
gamelogs_df4 = gamelogs.get_data_frames()[0]
gamelogs = playergamelog.PlayerGameLog(player_id = '1627734',season = '2019')
gamelogs_df5 = gamelogs.get_data_frames()[0]
gamelogs = playergamelog.PlayerGameLog(player_id = '1628369',season = '2019')
gamelogs_df6 = gamelogs.get_data_frames()[0]
gamelogs = playergamelog.PlayerGameLog(player_id = '1626167',season = '2019')
gamelogs_df7 = gamelogs.get_data_frames()[0]
gamelogs = playergamelog.PlayerGameLog(player_id = '1628389',season = '2019')
gamelogs_df8 = gamelogs.get_data_frames()[0]









