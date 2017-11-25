from django.db import models
from django.contrib.auth.models import User

class ProfileManager(models.Manager):
    def rank_profiles(self):
        profiles = self.all().order_by('-points')
        lastPoints = -1
        rank = 0
        for profile in profiles:
            if profile.points != lastPoints:
                rank += 1
            lastPoints = profile.points
            profile.rank = rank
            profile.save()
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    points = models.IntegerField()
    rank = models.IntegerField()
    objects = ProfileManager()
    def __str__(self):
        return self.user.username
        
    