from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name="index"),
    url(r'^fund/$', views.FundView.as_view(), name="fund"),
    url(r'^fund/(?P<fund_id>[0-9]+)/$', views.FundView.as_view(), name="fund"),
    url(r'^login/$', views.Login.as_view(), name="login"),
    url(r'^logout/$', views.Logout.as_view(), name="logout"),
    url(r'^buffer/$', views.BufferView.as_view(), name="buffer")
)
