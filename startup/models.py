from django.db import models
from django.contrib.auth.models import User

class StartupModel(models.Model):
    pass

class UserModel(User):
    user_price = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.username
