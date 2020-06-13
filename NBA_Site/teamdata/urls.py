from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='teamdata-home'),
    path('api/', views.ApiData.as_view(), name='teamdata-api'),
    path('glossary/', views.glossary, name='teamdata-glossary'),
    path('<str:team_abbr>/', views.team, name='teamdata-team'),
]