from django.contrib import admin
from .models import Problem, Category, Solution, Comment

# Register your models here.
admin.site.register(Problem)
admin.site.register(Category)
admin.site.register(Solution)
admin.site.register(Comment)