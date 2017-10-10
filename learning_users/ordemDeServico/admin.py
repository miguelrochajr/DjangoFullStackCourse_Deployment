from django.contrib import admin
from . import models
# Register your models here.

# NOTE: We don't need to register nothing here because we are using
# the Django's built in login and logout models

admin.site.register(models.OrdemDeServico)
