from django.db import models
from django.contrib.auth.models import User
from problems.models import Problem, Solution
from oauth2client.contrib.django_util.models import CredentialsField


class Organization(models.Model):
    # id (auto created)
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'media/_uploads/', blank=True)
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
    def recalculate_points(self):
        problems = Problem.objects.filter(isSolved=True)
        profiles = Profile.objects.all()
        for profile in profiles:
            profile.points = 0
            profile.rank = 0
            profile.save()
            
        for problem in problems:
            try:
                solution = Solution.objects.get(problem=problem, isChosen=True)
                profile = Profile.objects.get(user=solution.owner)
                profile.points += problem.points
                profile.save()
            except Exception as e:
                pass
        self.rank_profiles()
            
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
    image = models.ImageField(upload_to = 'media/_uploads/', blank=True)
    objects = ProfileManager()
    credential = CredentialsField(blank=True)
    def __str__(self):
        return self.user.username
        
    