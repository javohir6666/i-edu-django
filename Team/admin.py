from django.contrib import admin
from Team.models import Worker, TeamCategory
# Register your models here.
class AdminTeam(admin.ModelAdmin):
    list_display = ('name', 'surname', 'position')
admin.site.register(TeamCategory)
admin.site.register(Worker, AdminTeam)