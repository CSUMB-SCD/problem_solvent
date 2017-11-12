from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    points = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return self.user.username