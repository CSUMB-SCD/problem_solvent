from django.shortcuts import render, redirect
from .models import Problem, Comment, Solution
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils import timezone


from django import forms
from .models import Problem

class ProblemForm(forms.ModelForm):

    class Meta:
        model = Problem
        fields = ('title', 'description', 'long_description', 'category', 'points', 'image')
        
class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'cols': 10, 'rows': 5}),
        }
        labels = {
            "text": "Solution Description"
        }

# Create your views here.
def index(request, page=1):
    posts_per_page = 3
    page = int(page) - 1
    start = page*posts_per_page
    end = start + posts_per_page
    problems = Problem.objects.filter(isSolved=False)
    if start >= len(problems):
        return redirect('problems')
    if end > len(problems):
        end = len(problems)
    problems_subset = problems[start:end]
    
    if posts_per_page * (page + 1) >= len(problems):
        next_page = False
    else:
        next_page = page + 1 + 1 # increment and move offset for start by 1
    if page > 0:
        prev_page = page - 1 + 1 # decrement and move offset for start by 1
    else:
        prev_page = False
        
    return render(request, 'problems.html', {'problems': problems_subset, 'next_page': next_page, 'prev_page': prev_page})
    
def problem(request, id):
    if id != None:
        problem = Problem.objects.get(id=id)
        if problem:
            comments = Comment.objects.filter(problem=problem)
            solutions = Solution.objects.filter(problem=problem)
            sol_form = SolutionForm()
            return render(request, 'problem.html', {"problem":problem, "comments": comments, "solutions": solutions, "solution_form": sol_form})
    return redirect('problems')


@login_required(login_url="/login")
def solution(request, problem_id):
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.owner = request.user
            solution.likes = 0
            solution.problem = Problem.objects.get(id=problem_id)
            solution.date = timezone.now()
            solution.save()
    return redirect('/problem/' + str(problem_id))

@login_required(login_url="/login")
def new_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.owner = request.user
            problem.created = timezone.now()
            problem.save()
            return redirect('/problem/' + str(problem.id))
        else:
            print(form.errors)
            return render(request, 'new_problem.html', {'form': form})
    else:
        form = ProblemForm()
        return render(request, 'new_problem.html', {'form': form})
    