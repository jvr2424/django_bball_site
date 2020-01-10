from django.contrib import admin

# Register your models here.
from .models import Team, TeamMiscData

admin.site.register(Team)
admin.site.register(TeamMiscData)