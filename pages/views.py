from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    return render(request, 'index_new.html')
    
def problems(request):
    return render(request, 'problems.html')
    
def account(request):
    return render(request, 'account.html')
    
def leaderboard(request):
    return render(request, 'leaderboard.html')
    
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()
    print(request)
    return render(request, 'db.html', {'greetings': greetings})

