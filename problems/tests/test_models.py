from django.test import TestCase
from problems.models import Problem, Category, Solution
from django.utils import timezone

class ProblemModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cat = Category()
        cat.name = "Fishing"
        cat.save()
        
        problem = Problem()
        problem.title='World Peace'
        problem.created = timezone.now()
        problem.points = 10
        problem.category = Category.objects.get(name="Fishing")
        problem.save()
        
    def test_title_name_max_length(self):
        problems=Problem.objects.all()
        self.assertTrue(problems)
        
        
class SolutionModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        solution = Solution()
        solution.text = "Try using dynamite"
        solution.date = timezone.now()
        solution.likes = 0
        
        solution.save()
        
    def test_title_name_max_length(self):
        solutions=Solution.objects.all()
        self.assertTrue(solutions)