from django.conf.urls import patterns, include, url
import allauth
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    #All Auth URLS
    url(r'^accounts/', include('allauth.urls')),

    #Admin Urls
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)