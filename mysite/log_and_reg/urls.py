from django.conf.urls import patterns, include, url
from log_and_reg.views import reg_view,login_view,thanks

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^register/$',reg_view),
    (r'^login/$',login_view),
    (r'^loggedin/$',reg_view),
)
