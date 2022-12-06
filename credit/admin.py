from django.contrib import admin

from . import models

admin.site.register(models.Client)
admin.site.register(models.Account)
admin.site.register(models.Credit)