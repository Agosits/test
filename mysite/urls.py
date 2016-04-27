from django.conf.urls import patterns, include, url

from django.contrib import admin
from mysite.views import hello,current_datetime,hours_ahead
from mysite.books import urls as books_urls
#from mysite.contact import urls as contact_urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ('^hello/$',hello),
    ('^time/$',current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^books/',include(books_urls)),
    #(r'^contact/',include(contact.urls)),
    #(r'^account/',include(log_and_reg.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
