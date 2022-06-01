from django.contrib import admin
from Team.models import Worker, TeamCategory
from modeltranslation.admin import TranslationAdmin
# Register your models here.
class AdminTeam(TranslationAdmin):
    list_display = ('name', 'surname', 'position')
class AdminCategory(TranslationAdmin):
    list_display = ('title', 'desc')
admin.site.register(Worker, AdminTeam)
admin.site.register(TeamCategory, AdminCategory)