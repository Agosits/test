from django.conf.urls import patterns, include, url
from mysite.books.views import search

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),,
    (r'^search/$',search),
)