from django.shortcuts import render, redirect
from .models import Problem

# Create your views here.
def index(request):
    problems = Problem.objects.all()
    print("Index")
    return render(request, 'problems.html', {'problems': problems})
def problem(request, id):
    if id != None:
        problem = Problem.objects.get(id=id)
        if problem:
            return render(request, 'problem.html', {"problem":problem})

    return redirect('problems')