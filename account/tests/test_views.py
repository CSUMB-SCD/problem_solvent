from django.test import TestCase

from account import views

from problems.models import Problem, Solution
from django.urls import reverse
from django.core.management import call_command
from django.test.client import Client
from django.contrib.auth.models import User

# Create your tests here.
class AccountPageTestViews(TestCase):
    def setUp(self):
        call_command("loaddata", 'data_test.json', verbosity=0)
        self.client = Client()
        self.user = User.objects.get(username='prob_solv')
    
    def test_users_own_account_page(self):
        """
        Check user's own account shows proper information and buttons
        """
        
        self.client.force_login(self.user)
        response = self.client.get(reverse(views.index))
        self.assertContains(response, self.user.username)
        self.assertContains(response, "Edit Account")
        self.assertContains(response, "Change Password")
        
        # check to see if problems posted is shown
        problems = Problem.objects.filter(owner=self.user)
        self.assertContains(response, problems[0].title)
        
        # check to see if solutions posted is shown
        solutions = Solution.objects.filter(owner=self.user)
        self.assertContains(response, solutions[0].text)
        
        self.assertContains(response, 'Log out')
        self.assertEqual(response.status_code, 200)
    
    def test_different_user_account_page(self):
        """
        Check user can view another user's account and cannot edit settings
        """
        self.client.force_login(self.user)
        response = self.client.get('/account/nigeljames.12/')
        self.assertNotContains(response, "Edit Account")
        self.assertNotContains(response, "Change Password")
        self.assertContains(response, 'Log out')
        self.assertEqual(response.status_code, 200)
        
    def test_user_edit_account(self):
        """
        Logged in user can view their own edit account form/page
        """
        self.client.force_login(self.user)
        response = self.client.get('/editaccount/')
        self.assertEquals(response.status_code, 200)
    
    def test_anon_account_redirect(self):
        """
        Check if user not logged in is redirected
        """
        response = self.client.get('/account/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        
    def test_anon_specific_account(self):
        """
        Check if anonymous user can view any specific account
        """
        response = self.client.get('/account/nigeljames.12/')
        self.assertContains(response, 'nigeljames.12')
        self.assertNotContains(response, "Edit Account")
        self.assertNotContains(response, "Change Password")
        self.assertEqual(response.status_code, 200)
        
    def test_anon_edit_account_redirect(self):
        """
        Check if anonymous user is redirected if they somehow reach editaccount
        """
        response = self.client.get('/editaccount/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/editaccount/')