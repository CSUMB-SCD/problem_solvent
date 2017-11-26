from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    # id (auto created)
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    
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
            
        orgs = Organization.objects.all()
        for org in orgs:
            profiles = self.filter(organization=org)
            org_points = 0
            for profile in profiles:
                org_points += profile.points
            org.points = org_points
            org.save()
        
        orgs = Organization.objects.all().order_by('-points')
        lastPoints = -1
        rank = 0
        for org in orgs:
            if org.points != lastPoints:
                rank += 1
            lastPoints = org.points
            org.rank = rank
            org.save()
            
            
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    points = models.IntegerField()
    rank = models.IntegerField()
    org_rank = models.IntegerField()
    organization = models.ForeignKey('Organization', on_delete=models.SET_NULL, null=True, blank=True)
    objects = ProfileManager()
    def __str__(self):
        return self.user.username
        
    