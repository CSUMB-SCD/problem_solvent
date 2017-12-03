from django.test import TestCase
from problems.models import Problem


class ProblemModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Problem.objects.create(title='World Peace')
    
    
    def test_title_name_max_length(self):
        title=Problem.objects.get(id=1)
        max_length = title._meta.get_field('title').max_length
        self.assertEquals(max_length,100)
