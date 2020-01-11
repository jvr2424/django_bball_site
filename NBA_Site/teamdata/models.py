from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# each class is a table

class Team(models.Model):
    # these are fields
    conference = models.CharField(max_length=150)
    full_name = models.CharField(max_length=150)
    nick_name = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    abbr = models.CharField(max_length=150)
    nba_stats_team_id = models.IntegerField()
    alt_name = models.CharField(max_length=150, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("teamdata-team", kwargs={"team_abbr": self.abbr})

    def __str__(self):
        return self.abbr


class TeamMiscData(models.Model):
    team_name = models.ForeignKey('Team', on_delete=models.CASCADE)
    #	Age	W	L	PW	PL	MOV	SOS	SRS	ORtg	DRtg	NRtg	Pace	FTr	3PAr	TS%	eFG%	TOV%	ORB%	FT/FGA	eFG%	TOV%	DRB%	FT/FGA
    wins = models.IntegerField()
    losses = models.IntegerField()
    off_rtg = models.DecimalField(max_digits=7, decimal_places=1)
    def_rtg = models.DecimalField(max_digits=7, decimal_places=1)
    net_rtg = models.DecimalField(max_digits=7, decimal_places=1)
    pace = models.DecimalField(max_digits=7, decimal_places=1)
    ft_rate = models.DecimalField(max_digits=7, decimal_places=3)
    three_att_rate = models.DecimalField(max_digits=7, decimal_places=3)
    true_shooting_pct = models.DecimalField(max_digits=7, decimal_places=3)
    off_efg = models.DecimalField(max_digits=7, decimal_places=3)
    off_tov_pct = models.DecimalField(max_digits=7, decimal_places=1)
    orb_pct = models.DecimalField(max_digits=7, decimal_places=1)
    off_ft_per_fga = models.DecimalField(max_digits=7, decimal_places=3)
    def_efg = models.DecimalField(max_digits=7, decimal_places=3)
    def_tov_pct = models.DecimalField(max_digits=7, decimal_places=1)
    drb_pct = models.DecimalField(max_digits=7, decimal_places=1)
    def_ft_per_fga = models.DecimalField(max_digits=7, decimal_places=3)

    def __str__(self):
        return self.team_name.abbr


class TeamShooting(models.Model):
    # Rk	Team	G	MP	FG%	Dist.	2P	0-3	3-10	10-16	16-3pt	3P	2P	0-3	3-10	10-16	16-3pt	3P	%Ast'd	%FGA	Md.	%FGA	Md.	%Ast'd	%3PA	3P%	Att.	Md
    team_name = models.ForeignKey('Team', on_delete=models.CASCADE)
    morey_rate = models.DecimalField(max_digits=7, decimal_places=1, default=0.0)
    pct_2_pt_fga = models.DecimalField(max_digits=7, decimal_places=1)
    pct_0_3_ft_fga = models.DecimalField(max_digits=7, decimal_places=1)
    pct_3_10_ft_fga = models.DecimalField(max_digits=7, decimal_places=1)
    pct_10_16_ft_fga = models.DecimalField(max_digits=7, decimal_places=1)
    pct_16_3pt_fga = models.DecimalField(max_digits=7, decimal_places=1)
    pct_3pt_fga = models.DecimalField(max_digits=7, decimal_places=1)
    m_2_pt_fg_pct = models.DecimalField(max_digits=7, decimal_places=1)
    m_0_3_ft_fg_pct = models.DecimalField(max_digits=7, decimal_places=1)
    m_3_10_ft_fg_pct = models.DecimalField(max_digits=7, decimal_places=1)
    m_10_16_ft_fg_pct = models.DecimalField(max_digits=7, decimal_places=1)
    m_16_3pt_fg_pct = models.DecimalField(max_digits=7, decimal_places=1)
    m_3pt_fg_pct = models.DecimalField(max_digits=7, decimal_places=1)
    pct_astd_2_pt_fg = models.DecimalField(max_digits=7, decimal_places=1)
    pct_dunks_att = models.DecimalField(max_digits=7, decimal_places=1)
    pct_layups_att = models.DecimalField(max_digits=7, decimal_places=1)
    pct_corner_3_fga = models.DecimalField(max_digits=7, decimal_places=1)
    m_corner_3_fg_pct = models.DecimalField(max_digits=7, decimal_places=1)

    def __str__(self):
        return self.team_name.abbr
