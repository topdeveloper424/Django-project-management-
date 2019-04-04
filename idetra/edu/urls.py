# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [   
    url(r'^$', 'edu.views.edu', name='edu'),
    url(r'^(?P<slug>[-\w]+)/$', 'edu.views.course', name='course'),
    url(r'^(?P<slug_course>[-\w]+)/(?P<slug_lesson>[-\w]+)/$', 'edu.views.lesson', name='lesson'),
    url(r'^lessons/(?P<lesson_id>\d+)/update-progress/$', 'edu.views.update_lesson_progress', name='update_lesson_progress'),
    url(r'^comments/(?P<pk>\d+)/delete/$', 'edu.views.delete_comment', name='delete_comment')
]