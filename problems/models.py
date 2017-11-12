from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Problem(models.Model):
    # id (auto created)
    # Title string
    title = models.CharField(max_length=100)
    # Created by (User Id)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='user_owner')
    # Date created
    created = models.DateField()
    # IsSolved bool
    isSolved = models.BooleanField(default=False)
    # User id who solved problem
    user_solved = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='user_solved', null=True, blank=True)
    # description string
    description = models.CharField(max_length=500)
    # long description
    long_description = models.CharField(max_length=1500, default="Description not added.")
    # points possible int
    points = models.IntegerField()
    # category int relating to another table, (engineering, business, software, etc.)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=None)
    # image
    image = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    def toUrlId(self):
        fourCharString = str(self.id)
        while len(fourCharString) < 4:
            fourCharString = "0" + fourCharString


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name