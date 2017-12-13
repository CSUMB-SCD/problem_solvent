from django.test import TestCase
from django.core.management import call_command
from django.test.client import Client
from django.contrib.auth.models import User

from account.models import Profile
# Create your tests here.
class LeaderboardTest(TestCase):
    def setUp(self):
        call_command("loaddata", 'data_test.json', verbosity=0)
        self.client = Client()
        self.user = User.objects.get(username='prob_solv')
        self.profile = Profile.objects.get(user=self.user)

    def test_points_calculation(self):
        actual_points = self.profile.points
        # set points incorrect based on solutions accepted
        self.profile.points += 10
        self.profile.save()
        Profile.objects.recalculate_points()
        self.profile = Profile.objects.get(user=self.user)
        # check if points are properly calculated
        self.assertEquals(self.profile.points, actual_points)
        
    def test_ranking_calculation(self):
        pass