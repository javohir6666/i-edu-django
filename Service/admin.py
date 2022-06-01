from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from Service.models import ServiceModel
# Register your models here.
class AdminService(TranslationAdmin):
    list_display = ('title', 'add_time', 'price')
admin.site.register(ServiceModel, AdminService)
