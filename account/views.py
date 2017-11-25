from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from problems.models import Comment


# Create your views here.
@login_required(login_url='/login/')
def index(request):
    profile = Profile.objects.get(user=request.user)
    comments = Comment.objects.filter(owner=request.user)
    return render(request, "account.html", {"user": request.user, "profile": profile, "comments":comments})
    
    
def public_profile(request, userid):
    user = User.objects.get(id=userid)
    profile = Profile.objects.get(user=user)
    comments = Comment.objects.filter(owner=request.user)
    return render(request, "profile.html", {"user": request.user, "profile": profile, "comments":comments}) 
    
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile = Profile()
            profile.user = user
            profile.points = 0
            profile.rank = -1
            profile.save()
            Profile.objects.rank_profiles()
            login(request, user)
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})