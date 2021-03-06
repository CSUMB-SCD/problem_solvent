from django.shortcuts import render, redirect
from .models import Problem, Comment, Solution
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils import timezone


from django import forms
from .models import Problem
from account.models import Profile

class ProblemForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Problem
        fields = ('title', 'description', 'long_description', 'category', 'points', 'image')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 10, 'rows': 2}),
            'long_description': forms.Textarea(attrs={'cols': 10, 'rows': 5}),
        }
        
class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ('text', 'image')
        widgets = {
            'text': forms.Textarea(attrs={'cols': 10, 'rows': 5}),
        }
        labels = {
            "text": "Solution Description"
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            "text": "Comment"
        }

# Create your views here.
def index(request, page=1, solved=False):
    posts_per_page = 4
    page = int(page) - 1
    start = page*posts_per_page
    end = start + posts_per_page
    problems = Problem.objects.filter(isSolved=solved)
    
    if problems:
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
        
        return render(request, 'problems.html', {'problems': problems_subset, 'page': (page+1), 'next_page': next_page, 'prev_page': prev_page, 'solved': solved}, {'empty': False})
    else:
        return render(request, 'problems.html', {'empty': True})

def problem(request, id):
    if id != None:
        try:
            problem = Problem.objects.get(id=id)
            if problem:
                comments = Comment.objects.filter(problem=problem)
                solutions = Solution.objects.filter(problem=problem).order_by("-isChosen")
                sol_form = SolutionForm()
                comment_form = CommentForm()
                return render(request, 'problem.html', 
                {"problem":problem, "comments": comments, "solutions": solutions, "solution_form": sol_form, "comment_form":comment_form})
        except Exception as e:
            # problem id does not exist, redirect
            pass
    return redirect('problems')

@login_required(login_url="/login/")
def edit_problem(request, id):
    if id != None:
        problem = Problem.objects.get(id=id)
        if problem.owner != request.user:
            return redirect('/problem/' + str(problem.id) + '/')
        if request.method == 'POST':
            form = ProblemForm(request.POST, request.FILES, instance=problem)
            if form.is_valid():
                problem = form.save(commit=False)
                problem.save()
            else:
                print(form.errors)
            return redirect('/problem/' + str(problem.id) + '/')
        elif problem:
            problem_form = ProblemForm(instance=problem)
            return render(request, 'problem_form.html', {'form': problem_form, 'problem': problem, 'edit': True})
    return redirect('/problems/')
    
@login_required(login_url="/login/")
def delete_problem(request, id):
    if id != None:
        problem = Problem.objects.get(id=id)
        if problem.owner == request.user:
            Solution.objects.filter(problem=problem).delete()
            Comment.objects.filter(problem=problem).delete()
            problem.delete()
            Profile.objects.recalculate_points()
            return redirect('/problems/')
        else:
            return redirect('/problem/' + str(id) + '/')
    return redirect('/problems/')

@login_required(login_url="/login/")
def solution(request, problem_id):
    if request.method == 'POST':
        form = SolutionForm(request.POST, request.FILES)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.owner = request.user
            solution.likes = 0
            solution.problem = Problem.objects.get(id=problem_id)
            solution.date = timezone.now()
            solution.save()
    return redirect('/problem/' + str(problem_id) + '/')

@login_required(login_url="/login/")
def comment(request, problem_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = request.user
            comment.likes = 0
            comment.problem = Problem.objects.get(id=problem_id)
            comment.date = timezone.now()
            comment.save()
    return redirect('/problem/' + str(problem_id) + '/')
    
@login_required(login_url="/login/")
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    problem_id = comment.problem.id
    if comment.owner.id == request.user.id or comment.problem.owner.id == request.user.id:
        comment.delete()
    return redirect('/problem/' + str(problem_id) + '/')
    
@login_required(login_url="/login/")
def delete_solution(request, solution_id):
    solution = Solution.objects.get(id=solution_id)
    problem_id = solution.problem.id
    if (solution.owner.id == request.user.id or solution.problem.owner.id == request.user.id) and not solution.isChosen:
        solution.delete()
    return redirect('/problem/' + str(problem_id) + '/')
    
@login_required(login_url="/login/")
def select_solution(request, solution_id):
    solution = Solution.objects.get(id=solution_id)
    problem_id = solution.problem.id
    if solution.problem.owner.id == request.user.id and not solution.problem.isSolved:
        solution.isChosen = True
        solution.problem.isSolved = True
        solution.problem.save()
        solution.save()
        Profile.objects.recalculate_points()
    return redirect('/problem/' + str(problem_id) + '/')
    
@login_required(login_url="/login/")
def deselect_solution(request, solution_id):
    solution = Solution.objects.get(id=solution_id)
    problem_id = solution.problem.id
    if solution.problem.owner.id == request.user.id:
        solution.isChosen = False
        solution.problem.isSolved = False
        solution.problem.save()
        solution.save()
        Profile.objects.recalculate_points()
    return redirect('/problem/' + str(problem_id) + '/')

@login_required(login_url="/login/")
def new_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.owner = request.user
            problem.created = timezone.now()
            problem.save()
            return redirect('/problem/' + str(problem.id) + '/')
        else:
            print(form.errors)
            return render(request, 'problem_form.html', {'form': form})
    else:
        form = ProblemForm()
        return render(request, 'problem_form.html', {'form': form})
    