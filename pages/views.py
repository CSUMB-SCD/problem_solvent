from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        logged_in = True
    else:
        logged_in = False
    return render(request, 'index.html', {"home": True})
    
def problems(request):
    return render(request, 'problems.html')
    
# def account(request):
#     return render(request, '/account.html')
    
def leaderboard(request):
    return render(request, 'leaderboard.html')
    
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()
    print(request)
    return render(request, 'db.html', {'greetings': greetings})