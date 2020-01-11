from django.shortcuts import render
from django.http import HttpResponse
from .models import Team, TeamMiscData, TeamShooting




# Create your views here.
def home(request):
    context = {
        'teammiscdata': TeamMiscData.objects.all(),
        'teamshooting': TeamShooting.objects.all()
    }
    return render(request, 'teamdata/home.html', context)


def glossary(request):
    return render(request, 'teamdata/glossary.html', {'title': 'Glossary'})


def team(request, team_abbr):
    team = Team.objects.filter(abbr=team_abbr).first()
    team_misc = TeamMiscData.objects.filter(team_name=team).first()
    teamshooting = TeamShooting.objects.filter(team_name=team).first()
    context = {
        'title': team.abbr,
        'teammisc': team_misc,
        'teamshooting': teamshooting
    }
    return render(request, 'teamdata/team.html', context)