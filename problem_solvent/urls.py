from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from django.conf import settings
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
    url(r'^problems/([0-9]{1,})/$', problems.views.index, name='problems'),
    
    url(r'^problem/([0-9]{1,})/$', problems.views.problem, name='problem'),
    url(r'^solution/([0-9]{1,})/$', problems.views.solution, name='solution post'),
    url(r'^comment/([0-9]{1,})/$', problems.views.comment, name='comment post'),
    
    url(r'^delcomment/([0-9]{1,})/$', problems.views.delete_comment, name='comment delete'),
    url(r'^delsolution/([0-9]{1,})/$', problems.views.delete_solution, name='solution delete'),
    url(r'^selectsolution/([0-9]{1,})/$', problems.views.select_solution, name='solution select'),
    url(r'^deselectsolution/([0-9]{1,})/$', problems.views.deselect_solution, name='solution select'),

    
    url(r'^newproblem/$', problems.views.new_problem, name='new problem'),
    url(r'^editproblem/([0-9]{1,})/$', problems.views.edit_problem, name='edit problem'),

    url(r'^account/$', account.views.index, name='account'),
    url(r'^account/([0-9]{1,})/$', account.views.public_profile, name='account'),

    url(r'^leaderboard', leaderboard.views.index, name='leaderboard'),
    url(r'^oldchat', chat.views.index, name='oldchat'),
    url(r'^chat', chat_ws.views.index, name='chat'),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout),
    url(r'^signup/$', account.views.signup, name='signup')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)