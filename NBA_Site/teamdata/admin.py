from django.contrib import admin

# Register your models here.
from .models import Team, TeamMiscData, TeamShooting, DefensiveShooting

admin.site.register(Team)
admin.site.register(TeamMiscData)
admin.site.register(TeamShooting)
admin.site.register(DefensiveShooting)