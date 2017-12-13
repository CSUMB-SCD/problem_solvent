from django.test import TestCase

from account import views, models

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
        
    def test_non_existant_user_account_page(self):
        """
        Check user is redirected to their own account when trying to view non existant account
        """
        self.client.force_login(self.user)
        response = self.client.get('/account/nonexistantuser/')
        self.assertRedirects(response, '/account/')
        
    def test_user_edit_account(self):
        """
        Logged in user can view their own edit account form/page
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse(views.edit_account))
        self.assertEquals(response.status_code, 200)
        
    def test_user_change_password(self):
        """
        Logged in user can view their own change password form/page
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse(views.change_password))
        self.assertEquals(response.status_code, 200)
        
    def test_signup_page_view(self):
        """
        Test if user can view signup screen
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse(views.signup))
        self.assertEquals(response.status_code, 200)
    
    def test_signup_page_form(self):
        """
        Test creating a user with UserProfileCreateForm
        """
        temp_user_name = 'test_user_temp'
        form = views.UserProfileCreateForm({
            'username': temp_user_name,
            'password1': 'pass123##',
            'password2': 'pass123##',
            'email': 'email@email.com',
            'organization': models.Organization.objects.all()[0].id
        })
        self.assertTrue(form.is_valid())
        form.save()
        new_test_user = User.objects.get(username=temp_user_name)
        self.assertTrue(new_test_user)
        
    def test_edit_user_form(self):
        """
        Test change email/info of existing user
        """
        new_email = 'new_email@email.com'
        form = views.UserChangeForm({'email': new_email}, instance=models.Profile.objects.get(user=self.user))
        self.assertTrue(form.is_valid())
        form.save()
        # get updated user object
        self.user = User.objects.get(username=self.user.username)
        self.assertEquals(self.user.email, new_email)
        
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