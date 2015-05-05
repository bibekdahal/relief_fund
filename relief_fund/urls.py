from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'relief_fund.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mainapp/', include('mainapp.urls', namespace='mainapp')),
    url(r'^$', include('mainapp.urls', namespace='mainapp')),
)
