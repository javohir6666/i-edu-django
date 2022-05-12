from django.contrib import admin
from Service.models import ServiceModel
# Register your models here.
class AdminService(admin.ModelAdmin):
    list_display = ('title', 'add_time', 'price')
admin.site.register(ServiceModel, AdminService)
