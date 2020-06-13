from django.shortcuts import render
from django.http import HttpResponse
from .models import Team, TeamMiscData, TeamShooting, DefensiveShooting
from django.views.generic import View
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def home(request):
    offShooting = TeamShooting.objects.all().order_by('team_name')
    defShooting = DefensiveShooting.objects.all().order_by('team_name')
    miscData = TeamMiscData.objects.all().order_by('team_name')
    joinOffDefDict = []

    for x in range(0, 30):
        dict = {
            'team_name': offShooting[x].team_name,
            'wins': miscData[x].wins,
            'losses': miscData[x].losses,
            'net_rtg': miscData[x].net_rtg,
            'off_morey_rate': offShooting[x].morey_rate,
            'def_morey_rate': defShooting[x].morey_rate,
            'off_minus_def_morey_rt': offShooting[x].morey_rate - defShooting[x].morey_rate
        }
        joinOffDefDict.append(dict)

    context = {
        'teammiscdata': miscData,
        'teamshooting': offShooting,
        'oppshooting': defShooting,
        'joineddata': joinOffDefDict
    }
    return render(request, 'teamdata/home.html', context)


def glossary(request):
    return render(request, 'teamdata/glossary.html', {'title': 'Glossary'})


def team(request, team_abbr):
    team = Team.objects.filter(abbr=team_abbr).first()
    if team != None:
        team_misc = TeamMiscData.objects.filter(team_name=team).first()
        teamshooting = TeamShooting.objects.filter(team_name=team).first()
        context = {
            'title': team.abbr,
            'teammisc': team_misc,
            'teamshooting': teamshooting
        }
    else:
        context = {}
    return render(request, 'teamdata/team.html', context)



class ApiData(View):
    def get(self, request):
        team = Team.objects.filter(abbr='NYK').first()

        return JsonResponse(team)