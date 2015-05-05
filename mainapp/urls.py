from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'relief_fund.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.Index.as_view(), name="index"),
    url(r'^admin/', include(admin.site.urls)),
)
