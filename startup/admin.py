from django.contrib import admin
from .models import UserModel, StartupModel

admin.site.register([UserModel, StartupModel])

