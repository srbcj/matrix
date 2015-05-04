# coding:utf-8

from django.conf.urls import *
from matrix.view import hello
from inventory.testdb import appenddb
from inventory.testdb import deldb
from inventory.testdb import visitdb
from inventory.testdb import updatedb

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^testdb/$', appenddb),
    ('^deldb/$', deldb),
    ('^visitdb/$', visitdb),
    ('^updatedb/$', updatedb),
    # Examples:
    # url(r'^$', 'matrix.views.home', name='home'),
    # url(r'^matrix/', include('matrix.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
