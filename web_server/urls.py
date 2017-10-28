from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import pages.views
import chat.views

# Examples:
# url(r'^$', 'web_server.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', pages.views.index, name='index'),
    url(r'^db', pages.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^problems', pages.views.problems, name='problems'),
    url(r'^account', pages.views.account, name='account'),
    url(r'^leaderboard', pages.views.leaderboard, name='leaderboard'),


    url(r'^chat', chat.views.index, name='chat')
]
