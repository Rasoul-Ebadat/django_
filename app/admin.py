from django.contrib import admin
from . import models

#admin.site.register(models.Karshenas)

@admin.register(models.Karshenas)
class KarshenasAdmin(admin.ModelAdmin):
    #fields=[('karshenas_id'),('karshenas_title')]
    fields=[('karshenas_id','karshenas_title')]
