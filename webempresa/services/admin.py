from django.contrib import admin
from django.db import models
from .models import Service

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)