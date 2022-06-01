from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import PageModel
# Register your models here.
class AdminPage(TranslationAdmin):
    list_display = ('title', 'slug', 'add_time', 'seo_keywords')
admin.site.register(PageModel, AdminPage)