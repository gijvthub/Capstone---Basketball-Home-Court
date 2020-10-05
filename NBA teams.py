from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
teams_list = teams.get_teams()

allteams = [team for team in teams_list if team['abbreviation'] =='CHA'][0]
teamid = allteams['id']


teamresults = leaguegamefinder.LeagueGameFinder(team_id_nullable=teamid).get_data_frames()[0]
seasonyear = teamresults['SEASON_ID']=='22019'
currentyeargames = teamresults[seasonyear]
print(currentyeargames.shape)
print(currentyeargames)


