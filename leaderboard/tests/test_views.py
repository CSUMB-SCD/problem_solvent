from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from django.urls import reverse
from leaderboard import views

class LeaderboardTest(TestCase):
    def setUp(self):
        pass

    def test_leaderboard_view(self):
        response = self.client.get(reverse(views.index))
        self.assertEquals(response.status_code, 200)