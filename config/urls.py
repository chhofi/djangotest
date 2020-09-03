# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    path(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),

    # Django Admin
    path(r'^admin/', admin.site.urls),

    # User management
    path('^login/', auth_views.LoginView, name='login'),
    path('^logout/', auth_views.LogoutView, name='logout'),
    path(r'^users/', include('djangotest.users.urls', namespace='users'),

    # Rest
    path(r'^api/', include('djangotest.users.api.urls')),
    path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider'))

    # Your stuff: custom urls includes go here


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(r'^400/$', 'django.views.defaults.bad_request'),
        path(r'^403/$', 'django.views.defaults.permission_denied'),
        path(r'^404/$', 'django.views.defaults.page_not_found'),
        path(r'^500/$', 'django.views.defaults.server_error'),
    ]
