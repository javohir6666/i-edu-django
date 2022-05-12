from django.contrib import admin
from .models import PageModel
# Register your models here.
class AdminPage(admin.ModelAdmin):
    list_display = ('title', 'slug', 'add_time', 'seo_keywords')
admin.site.register(PageModel, AdminPage)