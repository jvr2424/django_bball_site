from bs4 import BeautifulSoup
from teamdata.models import Team

#TO RUN THIS
#python manage.py runscript updateTeamDB


def run():
    # start with team names
    # full_name = models.CharField()
    # nick_name = models.CharField()
    # city = models.CharField()
    # abbr = models.CharField()
    # nba_stats_team_id = models.IntegerField()
    # alt_name = models.CharField()
    Team.objects.all().delete()
    teamdict = [
        {
            'nick_name': 'Hawks',
            'city': 'Atlanta',
            'abbr': 'ATL',
            'nba_stats_team_id': '1610612737',
            'alt_name': None,
            'conference': 'East'
        },
        {
            'nick_name': 'Nets',
            'city': 'Brooklyn',
            'abbr': 'BKN',
            'nba_stats_team_id': '1610612751',
            'alt_name': None,
            'conference': 'East'
        },
        {
            'nick_name': 'Celtics',
            'city': 'Boston',
            'abbr': 'BOS',
            'nba_stats_team_id': '1610612738',
            'alt_name': None,
            'conference': 'East'
        },
        {
            'nick_name': 'Hornets',
            'city': 'Charlotte',
            'abbr': 'CHA',
            'nba_stats_team_id': '1610612766',
            'alt_name': None,
            'conference': 'East'
        },
        {
            'nick_name': 'Bulls',
            'city': 'Chicago',
            'abbr': 'CHI',
            'nba_stats_team_id': '1610612741',
            'alt_name': None,
            'conference': 'East'
        },
        {
            'nick_name': 'Cavaliers',
            'city': 'Cleveland',
            'abbr': 'CLE',
            'nba_stats_team_id': '1610612739',
            'alt_name': 'Cavs',
            'conference': 'East'
        },
        {
            'nick_name': 'Mavericks',
            'city': 'Dallas',
            'abbr': 'DAL',
            'nba_stats_team_id': '1610612742',
            'alt_name': 'Mavs',
            'conference': 'West'
        },
        {
            'nick_name': 'Nuggets',
            'city': 'Denver',
            'abbr': 'DEN',
            'nba_stats_team_id': '1610612743',
            'alt_name': None,
            'conference': 'West'
        },
        {
            'nick_name': 'Pistons',
            'city': 'Detroit',
            'abbr': 'DET',
            'nba_stats_team_id': '1610612765',
            'alt_name': None,
            'conference': 'East'
        },
        {
            'nick_name': 'Warriors',
            'city': 'Golden State',
            'abbr': 'GSW',
            'nba_stats_team_id': '1610612744',
            'alt_name': None,
            'conference': 'West'
        },
        {
            'nick_name': 'Rockets',
            'city': 'Houston',
            'abbr': 'HOU',
            'nba_stats_team_id': '1610612745',
            'alt_name': None,
            'conference': 'West'
        },
        {
            'nick_name': 'Pacers',
            'city': 'Indiana',
            'abbr': 'IND',
            'nba_stats_team_id': '1610612754',
            'alt_name': None,
            'conference': 'East'
        },
        {
            'nick_name': 'Clippers',
            'city': 'Los Angeles',
            'abbr': 'LAC',
            'nba_stats_team_id': '1610612746',
            'alt_name': 'LA Clippers',
            'conference': 'West'
        },
        {
            'nick_name': 'Lakers',
            'city': 'Los Angeles',
            'abbr': 'LAL',
            'nba_stats_team_id': '1610612747',
            'alt_name': 'LA Lakers',
            'conference': 'West'
        },
        {
            'nick_name': 'Grizzlies',
            'city': 'Memphis',
            'abbr': 'MEM',
            'nba_stats_team_id': '1610612763',
            'alt_name': 'Griz',
            'conference': 'West'
        },
        {
            'nick_name': 'Heat',
            'city': 'Miami',
            'abbr': 'MIA',
            'nba_stats_team_id': '1610612748',
            'alt_name': None,
            'conference': 'East'
        },
        {
            'nick_name': 'Bucks',
            'city': 'Milwaukee',
            'abbr': 'MIL',
            'nba_stats_team_id': '1610612749',
            'alt_name': None,
            'conference': 'East'
        },
        {
            'nick_name': 'Timberwolves',
            'city': 'Minnesota',
            'abbr': 'MIN',
            'nba_stats_team_id': '1610612750',
            'alt_name': 'Wolves',
            'conference': 'West'
        },
        {
            'nick_name': 'Pelicans',
            'city': 'New Orleans',
            'abbr': 'NOP',
            'nba_stats_team_id': '1610612740',
            'alt_name': 'Pels',
            'conference': 'West'
        },
        {
            'nick_name': 'Knicks',
            'city': 'New York',
            'abbr': 'NYK',
            'nba_stats_team_id': '1610612752',
            'alt_name': None,
            'conference': 'East'
        },
        {
            'nick_name': 'Thunder',
            'city': 'Oklahoma City',
            'abbr': 'OKC',
            'nba_stats_team_id': '1610612760',
            'alt_name': None,
            'conference': 'West'
        },
        {
            'nick_name': 'Magic',
            'city': 'Orlando',
            'abbr': 'ORL',
            'nba_stats_team_id': '1610612753',
            'alt_name': None,
            'conference': 'East'
        },
        {
            'nick_name': '76ers',
            'city': 'Philadelphia',
            'abbr': 'PHI',
            'nba_stats_team_id': '1610612755',
            'alt_name': 'Sixers',
            'conference': 'East'
        },
        {
            'nick_name': 'Suns',
            'city': 'Phoenix',
            'abbr': 'PHX',
            'nba_stats_team_id': '1610612756',
            'alt_name': None,
            'conference': 'West'
        },
        {
            'nick_name': 'Trail Blazers',
            'city': 'Portland',
            'abbr': 'POR',
            'nba_stats_team_id': '1610612757',
            'alt_name': 'Blazers',
            'conference': 'West'
        },
        {
            'nick_name': 'Kings',
            'city': 'Sacramento',
            'abbr': 'SAC',
            'nba_stats_team_id': '1610612758',
            'alt_name': None,
            'conference': 'West'
        },
        {
            'nick_name': 'Spurs',
            'city': 'San Antonio',
            'abbr': 'SAS',
            'nba_stats_team_id': '1610612759',
            'alt_name': None,
            'conference': 'West'
        },
        {
            'nick_name': 'Raptors',
            'city': 'Toronto',
            'abbr': 'TOR',
            'nba_stats_team_id': '1610612761',
            'alt_name': None,
            'conference': 'East'
        },
        {
            'nick_name': 'Jazz',
            'city': 'Utah',
            'abbr': 'UTA',
            'nba_stats_team_id': '1610612762',
            'alt_name': None,
            'conference': 'West'
        },
        {
            'nick_name': 'Wizards',
            'city': 'Washington',
            'abbr': 'WAS',
            'nba_stats_team_id': '1610612764',
            'alt_name': None,
            'conference': 'East'
        },
    ]
    for team in teamdict:
        newteam = Team(full_name=team['city'] + ' ' + team['nick_name'], nick_name=team['nick_name'], city=team['city'],
                       abbr=team['abbr'],nba_stats_team_id=team['nba_stats_team_id'], alt_name=team['alt_name'], conference=team['conference'])
        newteam.save()
