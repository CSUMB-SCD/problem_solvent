from django.conf.urls import include, url

from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

import pages.views
import chat_ws.views
import chat.views

# Examples:
# url(r'^$', 'problem_solvent.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', chat_ws.views.index, name='chat'),
    url(r'^index', pages.views.index, name='index'),
    url(r'^db', pages.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^problems', pages.views.problems, name='problems'),
    url(r'^user', pages.views.account, name='user'),
    url(r'^leaderboard', pages.views.leaderboard, name='leaderboard'),
    url(r'^oldchat', chat.views.index, name='oldchat'),
    url(r'^chat', chat_ws.views.index, name='chat'),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout)
]