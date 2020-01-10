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