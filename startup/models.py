from django.db import models
from django.contrib.auth.models import User

class StartupModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startup_name = models.CharField(max_length=200)
    startup_price = models.FloatField(default=0.0)
    startup_about = models.TextField(max_length=100000)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updeated = models.DateTimeField(auto_now=True, blank=True, null=True)

class UserModel(User):
    user_price = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.username
