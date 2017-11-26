from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Organization
from problems.models import Comment, Solution

from django import forms

class UserProfileCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    organization = forms.ModelChoiceField(queryset=Organization.objects.all())
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "organization")

    def save(self, commit=True):
        user = super(UserProfileCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            profile = Profile()
            profile.user = user
            profile.points = 0
            profile.rank = -1
            profile.org_rank = -1
            profile.organization = Organization.objects.get(name=self.cleaned_data["organization"])
            profile.save()
            Profile.objects.rank_profiles()
        return user

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    profile = Profile.objects.get(user=request.user)
    comments = Comment.objects.filter(owner=request.user)
    solutions = Solution.objects.filter(owner=request.user).order_by("-isChosen")
    num_prop_solutions = len(solutions)
    num_acc_solutions = 0
    
    for solution in solutions:
        if solution.isChosen:
            num_acc_solutions += 1
    return render(request, "account.html", {"user": request.user, "profile": profile, "solutions": solutions,
    "comments":comments, "num_prop_solutions":num_prop_solutions, "num_acc_solutions": num_acc_solutions })
    
    
def public_profile(request, userid):
    user = User.objects.get(id=userid)
    profile = Profile.objects.get(user=user)
    comments = Comment.objects.filter(owner=request.user)
    return render(request, "profile.html", {"user": request.user, "profile": profile, "comments":comments}) 
    
    
def signup(request):
    if request.method == 'POST':
        form = UserProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = UserProfileCreateForm()
    return render(request, 'signup.html', {'form': form})