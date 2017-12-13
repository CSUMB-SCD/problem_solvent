from django.test import TestCase

from django.urls import reverse
from problems import views
from problems.models import Problem
from django.core.management import call_command
from django.test.client import Client
from django.contrib.auth.models import User

class ProblemsAuthViewTests(TestCase):
    def setUp(self):
        call_command("loaddata", 'data_test.json', verbosity=0)
        self.client = Client()
        self.user = User.objects.get(username='prob_solv')
    
    def test_logged_in(self):
        """
        Check if nav bar shows "Log out" when user is logged in
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse(views.index))
        self.assertContains(response, 'Log out')
        self.assertEqual(response.status_code, 200)
    
    def test_delete_edit_button_owner(self):
        """
        Check if user can see delete and edit problem links on their own page
        """
        problems = Problem.objects.all()
        self.client.force_login(problems[0].owner)
        response = self.client.get(reverse(views.problem, args=[problems[0].id]))
        self.assertContains(response, 'Delete Problem')
        self.assertContains(response, 'Edit Problem')
        self.assertEqual(response.status_code, 200)
        
    def test_edit_problem_same_user(self):
        """
        Check if user can view form to edit their problem
        """
        problems = Problem.objects.all()
        self.client.force_login(problems[0].owner)
        response = self.client.get(reverse(views.edit_problem, args=[problems[0].id]))
        self.assertEqual(response.status_code, 200)
        
    def test_edit_problem_diff_user(self):
        """
        Check if user that doesn't own problem is redirected and can't edit
        """
        problems = Problem.objects.all()
        self.client.force_login(User.objects.get(username='nigeljames.12'))
        response = self.client.get(reverse(views.edit_problem, args=[problems[0].id]))
        self.assertRedirects(response, '/problem/' + str(problems[0].id) + '/')
        
    def test_delete_button_other_user(self):
        """
        Test to check if different user cannot see edit buttons on someone else's problem
        """
        problems = Problem.objects.all()
        self.client.force_login(User.objects.get(username='nigeljames.12'))
        response = self.client.get(reverse(views.problem, args=[problems[0].id]))
        self.assertNotContains(response, 'Delete Problem')
        self.assertEqual(response.status_code, 200)
        
    def test_new_problem_form(self):
        """
        Check if new problem form is rendered for a logged in user
        """
        self.client.force_login(self.user)
        response = self.client.get('/newproblem/')
        self.assertEqual(response.status_code, 200)

class ProblemsAnonViewTests(TestCase):
    # tests for each view when the user is not logged in
    def test_empty_view(self):
        """
        Test to check anon user can view page and message displays saying no problems
        """
        response = self.client.get(reverse(views.index))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no problems posted yet')
        self.assertContains(response, 'Log in')
        
    def test_empty_solved_view(self):
        """
        Test to check anon user can view page and message displays saying no solved problems
        """
        response = self.client.get(reverse(views.index, kwargs={'solved': True}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no problems posted yet")
    
    def test_anon_view_not_empty(self):
        """
        Test that anon can view problem feed and that problem is in feed
        """
        call_command("loaddata", 'data_test.json', verbosity=0)
        response = self.client.get('/problems/')
        self.assertEqual(response.status_code, 200)
        problems = Problem.objects.filter(isSolved=False)
        self.assertTrue(problems)
        self.assertContains(response, problems[0].title)
        
    def test_anon_view_not_empty_solved(self):
        """
        Test that anon can view solved problem feed and that problem is in feed
        """
        call_command("loaddata", 'data_test.json', verbosity=0)
        response = self.client.get(reverse(views.index, kwargs={'solved': True}))
        self.assertEqual(response.status_code, 200)
        problems = Problem.objects.filter(isSolved=True)
        self.assertTrue(problems)
        self.assertContains(response, problems[0].title)
        
    def test_new_problem_redirect(self):
        """ 
        Check if anon user is redirected when trying to create problem
        """
        response = self.client.get('/newproblem/')
        self.assertRedirects(response, '/login/?next=/newproblem/')