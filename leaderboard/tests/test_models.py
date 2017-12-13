from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory


from leaderboard.views import index

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_LeaderboardRank(self):
        # Create an instance of a GET request.
        request = self.factory.get('/leaderboard')
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = index(request)
        # get top ranked user, must be 
        # self.assertEqual(response)