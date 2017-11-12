from django.shortcuts import render, redirect
from .models import Problem, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    problems = Problem.objects.all()
    return render(request, 'problems.html', {'problems': problems})
def problem(request, id):
    if id != None:
        problem = Problem.objects.get(id=id)
        if problem:
            comments = Comment.objects.filter(problem=problem)

            return render(request, 'problem.html', {"problem":problem, "comments": comments})
    return redirect('problems')

@login_required
def new_problem(request):
    return render(request, 'new_problem.html')