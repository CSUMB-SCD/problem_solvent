from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    request.user
    return render(request, "account.html", {"user": request.user})