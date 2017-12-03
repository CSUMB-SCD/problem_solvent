from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Organization
from problems.models import Comment, Solution, Problem
from oauth2client.contrib import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from oauth2client.client import OAuth2WebServerFlow
import os
import problem_solvent.settings as settings

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
class ChangePassForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")
class UserChangeForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    # organization = forms.ModelChoiceField(queryset=Organization.objects.all())
    # image = forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields = ("email", "organization", "image" )
        
    def save(self, commit=True):
        self.instance.user.email = self.cleaned_data["email"]
        self.instance.user.save()
        self.instance.save()
        return self.instance

# Create your views here.
def index(request, username=False):
    if request.user.is_authenticated() and not username:
        full_access = True
    elif request.user.is_authenticated() and username == request.user.username:
        full_access = True
    else:
        full_access = False
    user = False
    if username:
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            if request.user.is_authenticated():
                return redirect('/account/')
            else:
                return redirect('/')
    if not user:
        user = request.user
    try: 
        profile = Profile.objects.get(user=user)
        comments = Comment.objects.filter(owner=user)
        solutions = Solution.objects.filter(owner=user).order_by("-isChosen")
        problems = Problem.objects.filter(owner=user)
        num_prop_solutions = len(solutions)
        num_acc_solutions = 0
        
        for solution in solutions:
            if solution.isChosen:
                num_acc_solutions += 1
        return render(request, "account.html", {"profile": profile, "solutions": solutions, "full_access": full_access,
        "comments":comments, "num_prop_solutions":num_prop_solutions, "num_acc_solutions": num_acc_solutions, "problems": problems })
    except Exception as e:
        if full_access:
            new_profile = Profile()
            new_profile.user = request.user
            new_profile.rank = 0
            new_profile.points = 0
            new_profile.org_rank = 0
            new_profile.save()
            Profile.objects.recalculate_points()
            return redirect('/account/')
        return redirect('/')

@login_required(login_url="/login")
def edit_account(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            user = form.save()
        else:
            print(form.errors)
            return render(request, 'account_form.html', {'form': form })
            
    info_form = UserChangeForm(instance=profile, initial={'email': profile.user.email})

    return render(request, 'account_form.html', {'form': info_form })
    
@login_required(login_url="/login")
def change_password(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/account/')
        else:
            print(form.errors)
            return render(request, 'account_form.html', {'form': form , 'password': True})
            
    form = PasswordChangeForm(request.user)

    return render(request, 'account_form.html', {'form': form, 'password':True })

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
    return render(request, 'account_form.html', {'form': form})
    

def temp_login(request):
    return render(request, 'social_login.html')

