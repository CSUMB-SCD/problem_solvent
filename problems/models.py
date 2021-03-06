from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Problem(models.Model):
    # id (auto created)
    # Title string
    title = models.CharField(max_length=100)
    # Created by (User Id)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='problem_owner')
    # Date created
    created = models.DateTimeField()
    # IsSolved bool
    isSolved = models.BooleanField(default=False)
    # User id who solved problem
    user_solved = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='user_solved', null=True, blank=True)
    # description string
    description = models.CharField(max_length=500)
    # long description
    long_description = models.CharField(max_length=1500)
    # points possible int
    points = models.IntegerField()
    # category int relating to another table, (engineering, business, software, etc.)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=None)
    # image
    image = models.ImageField(upload_to = 'media/_uploads/')
    
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey('Problem', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    text = models.CharField(max_length=280)
    def __str__(self):
        return self.text

    class Meta:
        abstract = True


class Solution(Post):
    models.OneToOneField(to=Post, parent_link=True, related_name="parent_post_solution")
    isChosen = models.BooleanField(default=False)
    image = models.ImageField(upload_to = 'media/_uploads/', blank=True, default=None, null=True)

class Comment(Post):
    models.OneToOneField(to=Post, parent_link=True, related_name="parent_post_comment")
    hidden = models.BooleanField(default=False)