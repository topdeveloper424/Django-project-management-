# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static
from registration.forms import RegistrationFormUniqueEmail
from registration.backends.default.views import RegistrationView

urlpatterns = [   
    url(r'^$', 'website.views.home', name='home'),
    url(r'^ci/', include('ci.urls', namespace='ci')),
    url(r'^edu/(?P<slug>[\w-]+)/', include('edu.urls', namespace='edu')),
    url(r'^profile/(?P<slug>[\w-]+)/$', 'website.views.profile', name='profile'),
    url(r'^dictionary/(?P<slug>[\w-]+)/$', 'website.views.dictionary', name='dictionary'),
    url(r'^comments/', include('fluent_comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/(?P<slug>[\w-]+)/$', RegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='registration_register'),
    url(r'^accounts/(?P<slug>[\w-]+)/$', include('registration.backends.default.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    url(_(r'^$'), 'website.views.home', name='home'),
    # url(_(r'^ci/'), include('ci.urls', namespace='ci')),
    url(_(r'^edu/'), include('edu.urls', namespace='edu')),
    url(_(r'^profile/'), 'website.views.profile', name='profile'),
    url(_(r'^dictionary/'), 'edu.views.dictionary', name='dictionary'),
    url(_(r'^comments/'), include('fluent_comments.urls')),
    url(_(r'^admin/'), include(admin.site.urls)),
    url(_(r'^accounts/register/$'), RegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='registration_register'),
    url(_(r'^accounts/'), include('registration.backends.default.urls')),
    
)
