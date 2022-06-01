from django.contrib import admin
from Project.models import ProjectModel
from modeltranslation.admin import TranslationAdmin
# Register your models here.
class AdminProject(TranslationAdmin):
    list_display=('ProjectName', 'add_time','website')
admin.site.register(ProjectModel, AdminProject)