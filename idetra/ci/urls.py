# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [   
    url(r'^$', 'ci.views.myarea', name='ci'),
    url(r'^project/', 'ci.views.project', name='project'),
    url(r'^assets/', 'ci.views.assets', name='assets'),

]
