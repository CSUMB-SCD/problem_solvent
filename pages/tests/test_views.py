from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from pages.views import index

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_home(self):
        # Create an instance of a GET request.
        request = self.factory.get('/')
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = index(request)
        self.assertEqual(response.status_code, 200)
        
    def test_login(self):
        # Create an instance of a GET request.
        request = self.factory.get('/login')
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = index(request)
        self.assertEqual(response.status_code, 200)
    
    def test_leaderboard(self):
        # Create an instance of a GET request.
        request = self.factory.get('/leaderboard')
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = index(request)
        self.assertEqual(response.status_code, 200)
    