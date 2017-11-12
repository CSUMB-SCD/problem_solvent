from django.conf.urls import include, url

from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

import pages.views
import chat_ws.views
import chat.views
import problems.views
import account.views
import leaderboard.views

# Examples:
# url(r'^$', 'problem_solvent.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^pubchat', chat_ws.views.index, name='chat'),
    url(r'^$', pages.views.index, name='index'),
    url(r'^db', pages.views.db, name='db'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^problems/$', problems.views.index, name='problems'),
    url(r'^problem/([0-9]{1})/$', problems.views.problem, name='problem'),
    url(r'^problem/([0-9]{2})/$', problems.views.problem, name='problem'),
    url(r'^problem/([0-9]{3})/$', problems.views.problem, name='problem'),
    url(r'^problem/([0-9]{4})/$', problems.views.problem, name='problem'),
    url(r'^newproblem/$', problems.views.new_problem, name='new problem'),\

    url(r'^account/$', account.views.index, name='account'),

    url(r'^leaderboard', leaderboard.views.index, name='leaderboard'),
    url(r'^oldchat', chat.views.index, name='oldchat'),
    url(r'^chat', chat_ws.views.index, name='chat'),
    url(r'^login/$', login),
    url(r'^logout/$', logout)

]