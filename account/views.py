from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from problems.models import Comment

# Create your views here.
@login_required
def index(request):
    profile = Profile.objects.get(user=request.user)
    comments = Comment.objects.filter(owner=request.user)
    return render(request, "account.html", {"user": request.user, "profile": profile, "comments":comments})