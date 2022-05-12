from django.contrib import admin
from Project.models import ProjectModel
# Register your models here.
class AdminProject(admin.ModelAdmin):
    list_display=('ProjectName', 'add_time','website')
admin.site.register(ProjectModel, AdminProject)