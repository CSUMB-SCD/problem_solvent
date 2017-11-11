from django.db import models

# Create your models here.
class Problem(models.Model):
    # id (auto created)
    # Title string
    title = models.CharField(max_length=100)
    # Created by (User Id)
    owner = models.IntegerField()
    # Date created
    created = models.DateField()
    # IsSolved bool
    isSolved = models.BooleanField(default=False)
    # User id who solved problem
    user_solved = models.IntegerField()
    # description string
    description = models.CharField(max_length=500)
    # points possible int
    points = models.IntegerField()
    # category int relating to another table, (engineering, business, software, etc.)
    category = models.IntegerField()
    # image
    image = models.CharField(max_length=100)
    def __str__(self):
        return self.title