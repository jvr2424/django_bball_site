import pandas as pd
from pandas.io.json import json_normalize 
import json
import requests
from datetime import datetime, timedelta



gameIDpage = requests.get('https://api.pbpstats.com/get-games/nba?Season=2019-20&SeasonType=Regular%2BSeason')
games = gameIDpage.json()


yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
game_date = yesterday_date
i = 1

while game_date == yesterday_date:
	game = games['results'][-i]
	i = i + 1
	game_ID = game['GameId']
	date = game['Date']
	game_date = date
	if game_date != yesterday_date:
		break

	print(game_ID)
	print(date)






	page = requests.get(f'https://api.pbpstats.com/get-game-stats?Type=Player&GameId={game_ID}')

	data = page.json()

	homeData = data['team_results']['Home']['FullGame']
	awayData = data['team_results']['Away']['FullGame']

	headersData = data['header_order_map']['Shooting']


	away_df = json_normalize(awayData)
	home_df  = json_normalize(homeData)

	headers_df = json_normalize(headersData)
	#headers_df.set_index('field')
	headers_df = headers_df.drop(['hover', 'label', 'type', 'minfilter'], axis=1)


	away_df_transposed = away_df.transpose()
	home_df_transposed = home_df.transpose()

	game_df = pd.merge(away_df_transposed,home_df_transposed, right_index=True, left_index=True, how='inner')
	game_df.columns = ['away', 'home']
	game_df['field'] = game_df.index

	shooting_df = pd.merge(headers_df, game_df,  on='field',  how='left')

	#print(game_df.head(30))
	print(shooting_df)


