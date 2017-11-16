from django.conf.urls import patterns, include, url
from django.contrib import admin
from masterdata.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'allautocomlete.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',home,name="mani"),
    url(r'^profiledata/$',profiledata,name="siva"),
)
