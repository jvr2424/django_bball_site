from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='teamdata-home'),
    path('glossary/', views.glossary, name='teamdata-glossary'),
    path('<str:team_abbr>/', views.team, name='teamdata-team'),
]