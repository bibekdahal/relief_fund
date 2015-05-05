from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name="index"),
    url(r'^fund/$', views.FundView.as_view(), name="fund"),
)
