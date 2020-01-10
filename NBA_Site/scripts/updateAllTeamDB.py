from bs4 import BeautifulSoup
import requests
import datetime
from teamdata.models import Team, TeamMiscData, TeamShooting
import re


def run():
    now = datetime.datetime.now()
    if now.month > 7:
        currentSeason = str(now.year + 1)
    else:
        currentSeason = str(now.year)
    getLatestMiscData(currentSeason)
    getLatestShootingData(currentSeason)


def getLatestShootingData(currentSeason):
    TeamShooting.objects.all().delete()
    # scrape the next 8 days worth of prime time NBA games
    page = requests.get('https://www.basketball-reference.com/leagues/NBA_' + currentSeason + '.html')
    soup = BeautifulSoup(page.content, 'html.parser')

    # find the misc stats table
    shootingtable = soup.find(string=re.compile('id="team_shooting"'))
    shootingtable = BeautifulSoup(shootingtable, 'html.parser')
    shootingtablerows = shootingtable.tbody.findAll('tr')
    for row in shootingtablerows:
        rowdata = row.findAll('td')
        for data in rowdata:
            # Rk	Team	G	MP	FG%	Dist.	2P	0-3	3-10	10-16	16-3pt	3P	2P	0-3	3-10	10-16	16-3pt	3P	%Ast'd	%FGA	Md.	%FGA	Md.	%Ast'd	%3PA	3P%	Att.	Md

            if data['data-stat'] == 'team_name':
                team_name = data.text
            elif data['data-stat'] == 'fg2a_pct_fga':
                pct_2_pt_fga = float(data.text) * 100
            elif data['data-stat'] == 'pct_fga_00_03':
                pct_0_3_ft_fga = float(data.text) * 100
            elif data['data-stat'] == 'pct_fga_03_10':
                pct_3_10_ft_fga = float(data.text) * 100
            elif data['data-stat'] == 'pct_fga_10_16':
                pct_10_16_ft_fga = float(data.text) * 100
            elif data['data-stat'] == 'pct_fga_16_xx':
                pct_16_3pt_fga = float(data.text) * 100
            elif data['data-stat'] == 'fg3a_pct_fga':
                pct_3pt_fga = float(data.text) * 100
            elif data['data-stat'] == 'fg2_pct':
                _2_pt_fg_pct = float(data.text) * 100
            elif data['data-stat'] == 'fg_pct_00_03':
                _0_3_ft_fg_pct = float(data.text) * 100
            elif data['data-stat'] == 'fg_pct_03_10':
                _3_10_ft_fg_pct = float(data.text) * 100
            elif data['data-stat'] == 'fg_pct_10_16':
                _10_16_ft_fg_pct = float(data.text) * 100
            elif data['data-stat'] == 'fg_pct_16_xx':
                _16_3pt_fg_pct = float(data.text) * 100
            elif data['data-stat'] == 'fg3_pct':
                _3pt_fg_pct = float(data.text) * 100
            elif data['data-stat'] == 'fg2_pct_ast':
                pct_astd_2_pt_fg = float(data.text) * 100
            elif data['data-stat'] == 'pct_fg2_dunk':
                pct_dunks_att = float(data.text) * 100
            elif data['data-stat'] == 'pct_fg2_layup':
                pct_layups_att = float(data.text) * 100
            elif data['data-stat'] == 'pct_fg3a_corner':
                pct_corner_3_fga = float(data.text) * 100
            elif data['data-stat'] == 'fg3_pct_corner':
                _corner_3_fg_pct = float(data.text) * 100
        #
        # team_name = models.ForeignKey('Team', on_delete=models.CASCADE)
        # pct_2_pt_fga = models.DecimalField(max_digits=7, decimal_places=3)
        # pct_0_3_ft_fga = models.DecimalField(max_digits=7, decimal_places=3)
        # pct_3_10_ft_fga = models.DecimalField(max_digits=7, decimal_places=1)
        # pct_10_16_ft_fga = models.DecimalField(max_digits=7, decimal_places=1)
        # pct_16_3pt_fga = models.DecimalField(max_digits=7, decimal_places=1)
        # pct_3pt_fga = models.DecimalField(max_digits=7, decimal_places=1)
        # _2_pt_fg_pct = models.DecimalField(max_digits=7, decimal_places=3)
        # _0_3_ft_fg_pct = models.DecimalField(max_digits=7, decimal_places=3)
        # _3_10_ft_fg_pct = models.DecimalField(max_digits=7, decimal_places=3)
        # _10_16_ft_fg_pct = models.DecimalField(max_digits=7, decimal_places=3)
        # _16_3pt_fg_pct = models.DecimalField(max_digits=7, decimal_places=1)
        # _3pt_fg_pct = models.DecimalField(max_digits=7, decimal_places=1)
        # pct_astd_2_pt_fg = models.DecimalField(max_digits=7, decimal_places=3)
        # pct_dunks_att = models.DecimalField(max_digits=7, decimal_places=3)
        # pct_layups_att = models.DecimalField(max_digits=7, decimal_places=1)
        # pct_corner_3_fga = models.DecimalField(max_digits=7, decimal_places=1)
        # _corner_3_fg_pct = models.DecimalField(max_digits=7, decimal_places=3)
        team_obj = Team.objects.filter(full_name=team_name).first()
        newshootingdata = TeamShooting(team_name=team_obj, morey_rate=pct_0_3_ft_fga + pct_3pt_fga,
                                       pct_2_pt_fga=pct_2_pt_fga, pct_0_3_ft_fga=pct_0_3_ft_fga,
                                       pct_3_10_ft_fga=pct_3_10_ft_fga, pct_10_16_ft_fga=pct_10_16_ft_fga,
                                       pct_16_3pt_fga=pct_16_3pt_fga,
                                       pct_3pt_fga=pct_3pt_fga, m_2_pt_fg_pct=_2_pt_fg_pct,
                                       m_0_3_ft_fg_pct=_0_3_ft_fg_pct,
                                       m_3_10_ft_fg_pct=_3_10_ft_fg_pct, m_10_16_ft_fg_pct=_10_16_ft_fg_pct,
                                       m_16_3pt_fg_pct=_16_3pt_fg_pct, m_3pt_fg_pct=_3pt_fg_pct,
                                       pct_astd_2_pt_fg=pct_astd_2_pt_fg,
                                       pct_dunks_att=pct_dunks_att, pct_layups_att=pct_layups_att,
                                       pct_corner_3_fga=pct_corner_3_fga,
                                       m_corner_3_fg_pct=_corner_3_fg_pct)
        newshootingdata.save()


def getLatestMiscData(currentSeason):
    TeamMiscData.objects.all().delete()

    page = requests.get('https://www.basketball-reference.com/leagues/NBA_' + currentSeason + '.html')

    # scrape the next 8 days worth of prime time NBA games
    soup = BeautifulSoup(page.content, 'html.parser')

    scrapedRow = {}
    allScrapedRows = []

    # find the misc stats table
    misctable = soup.find(string=re.compile('id="misc_stats"'))
    misctable = BeautifulSoup(misctable, 'html.parser')
    misctablerows = misctable.tbody.findAll('tr')
    for row in misctablerows:
        scrapedRow = {}
        rowdata = row.findAll('td')
        #	Age	W	L	PW	PL	MOV	SOS	SRS	ORtg	DRtg	NRtg	Pace	FTr	3PAr	TS%	eFG%	TOV%	ORB%	FT/FGA	eFG%	TOV%	DRB%	FT/FGA
        for data in rowdata:
            if data['data-stat'] == 'team_name':
                team_name = data.text
            elif data['data-stat'] == 'wins':
                wins = data.text
            elif data['data-stat'] == 'losses':
                losses = data.text
            elif data['data-stat'] == 'off_rtg':
                off_rtg = data.text
            elif data['data-stat'] == 'def_rtg':
                def_rtg = data.text
            elif data['data-stat'] == 'net_rtg':
                net_rtg = data.text
            elif data['data-stat'] == 'pace':
                pace = data.text
            elif data['data-stat'] == 'fta_per_fga_pct':
                fta_per_fga_pct = data.text
            elif data['data-stat'] == 'fg3a_per_fga_pct':
                fg3a_per_fga_pct = data.text
            elif data['data-stat'] == 'ts_pct':
                ts_pct = data.text
            elif data['data-stat'] == 'efg_pct':
                efg_pct = data.text
            elif data['data-stat'] == 'tov_pct':
                tov_pct = data.text
            elif data['data-stat'] == 'orb_pct':
                orb_pct = data.text
            elif data['data-stat'] == 'ft_rate':
                ft_rate = data.text
            elif data['data-stat'] == 'opp_efg_pct':
                opp_efg_pct = data.text
            elif data['data-stat'] == 'opp_tov_pct':
                opp_tov_pct = data.text
            elif data['data-stat'] == 'drb_pct':
                drb_pct = data.text
            elif data['data-stat'] == 'opp_ft_rate':
                opp_ft_rate = data.text
        team_obj = Team.objects.filter(full_name=team_name).first()
        scrapedRow = {
            'team_name': team_obj,
            'wins': wins,
            'losses': losses,
            'off_rtg': off_rtg,
            'def_rtg': def_rtg,
            'net_rtg': net_rtg,
            'pace': pace,
            'fta_per_fga_pct': fta_per_fga_pct,
            'fg3a_per_fga_pct': fg3a_per_fga_pct,
            'ts_pct': ts_pct,
            'efg_pct': efg_pct,
            'tov_pct': tov_pct,
            'orb_pct': orb_pct,
            'ft_rate': ft_rate,
            'opp_efg_pct': opp_efg_pct,
            'opp_tov_pct': opp_tov_pct,
            'drb_pct': drb_pct,
            'opp_ft_rate': opp_ft_rate
        }
        allScrapedRows.append(scrapedRow)
        newmiscdata = TeamMiscData(team_name=scrapedRow['team_name'], wins=scrapedRow['wins'],
                                   losses=scrapedRow['losses'],
                                   off_rtg=scrapedRow['off_rtg'], def_rtg=scrapedRow['def_rtg'],
                                   net_rtg=scrapedRow['net_rtg'],
                                   pace=scrapedRow['pace'], ft_rate=scrapedRow['fta_per_fga_pct'],
                                   three_att_rate=scrapedRow['fg3a_per_fga_pct'],
                                   true_shooting_pct=scrapedRow['ts_pct'],
                                   off_efg=scrapedRow['efg_pct'],
                                   off_tov_pct=scrapedRow['tov_pct'], orb_pct=scrapedRow['orb_pct'],
                                   off_ft_per_fga=scrapedRow['ft_rate'], def_efg=scrapedRow['opp_efg_pct'],
                                   def_tov_pct=scrapedRow['opp_tov_pct'],
                                   drb_pct=scrapedRow['drb_pct'], def_ft_per_fga=scrapedRow['opp_ft_rate'])
        newmiscdata.save()
    # team_name
    # wins = models.IntegerField()
    # losses = models.IntegerField()
    # off_rtg = models.DecimalField(max_digits=7, decimal_places=1)
    # def_rtg = models.DecimalField(max_digits=7, decimal_places=1)
    # net_rtg = models.DecimalField(max_digits=7, decimal_places=1)
    # pace = models.DecimalField(max_digits=7, decimal_places=1)
    # ft_rate = models.DecimalField(max_digits=7, decimal_places=3)
    # three_att_rate = models.DecimalField(max_digits=7, decimal_places=3)
    # true_shooting_pct = models.DecimalField(max_digits=7, decimal_places=3)
    # off_efg = models.DecimalField(max_digits=7, decimal_places=3)
    # off_tov_pct = models.DecimalField(max_digits=7, decimal_places=1)
    # off_orb_pct = models.DecimalField(max_digits=7, decimal_places=1)
    # off_ft_per_fga = models.DecimalField(max_digits=7, decimal_places=3)
    # def_efg = models.DecimalField(max_digits=7, decimal_places=3)
    # def_tov_pct = models.DecimalField(max_digits=7, decimal_places=1)
    # def_orb_pct = models.DecimalField(max_digits=7, decimal_places=1)
    # def_ft_per_fga = models.DecimalField(max_digits=7, decimal_places=3)

    # # add leage average data to last row
    # tablefooter = misctable.tfoot
    # ladata = tablefooter.findAll('td')
    # scrapedRow = []
    # allScrapedRows = []
    # for data in ladata:
    #     if data['data-stat'] == 'team_name' or data['data-stat'] == 'wins' or data['data-stat'] == 'losses' or data[
    #         'data-stat'] == 'off_rtg' or data['data-stat'] == 'def_rtg' or data['data-stat'] == 'net_rtg' or data[
    #         'data-stat'] == 'pace' or data['data-stat'] == 'ts_pct' or data['data-stat'] == 'tov_pct':
    #         scrapedRow.append(data.text)
    # allScrapedRows.append(scrapedRow)
    #
    # la_df = pd.DataFrame(allScrapedRows)
    # la_df['Win PCT'] = ''
    # la_df['Seed'] = ''
    # la_df.columns = df.columns
    #
    #
    # df = df.append(la_df, sort=False)
    # # re order columns
    # df = df[['Team Name', 'Seed', 'Wins', 'Losses', 'Win PCT', 'ORtg', 'DRtg', 'NRtg', 'Pace', 'TS', 'TOV']]
