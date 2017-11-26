from django.shortcuts import render
from account.models import Profile, Organization
# Create your views here.
def index(request):
    Profile.objects.rank_profiles()
    users = Profile.objects.all().order_by('rank')
    orgs = Organization.objects.all().order_by('rank')
    return render(request, "leaderboard.html", {"users": users, "orgs": orgs})