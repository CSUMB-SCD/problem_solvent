from django.test import TestCase
from problems.models import Problem, Category, Solution
from django.utils import timezone
from django.core.management import call_command
from django.test.client import Client
from django.contrib.auth.models import User


class ProblemModelTest(TestCase):
    
    def setUp(self):
        # Set up non-modified objects used by all test methods
        call_command("loaddata", 'data_test.json', verbosity=0)
        self.client = Client()
        self.user = User.objects.get(username='prob_solv')
        
        problem = Problem()
        problem.title='World Peace'
        problem.created = timezone.now()
        problem.points = 10
        problem.category = Category.objects.all()[0]
        problem.owner = self.user
        problem.save()
        
    def test_problem_str(self):
        
        
        problems=Problem.objects.all()
        self.assertTrue(problems)
        self.assertEquals(problems[0].title, str(problems[0]))
        
        
class SolutionModelTest(TestCase):
    
    def setUp(self):
        # Set up non-modified objects used by all test methods
        call_command("loaddata", 'data_test.json', verbosity=0)
        self.client = Client()
        self.user = User.objects.get(username='prob_solv')
        
        solution = Solution()
        solution.text = "Try using dynamite"
        solution.date = timezone.now()
        solution.owner = self.user
        solution.likes = 0
        
        solution.save()
        
    def test_solution_str(self):
        solutions=Solution.objects.all()
        self.assertTrue(solutions)
        self.assertEquals(solutions[0].text, str(solutions[0]))