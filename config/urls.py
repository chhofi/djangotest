# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.conf import settings
#from django.conf.urls import include, url
#from django.conf.urls.static import static
#from django.urls import path
#from django.contrib import admin
#from django.views.generic import TemplateView
#from django.contrib.auth import views as auth_views

#urlpatterns = [
#    path(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
#    path(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),
#
#    # Django Admin
#    path(r'^admin/', admin.site.urls),

    # User management
#    path('^login/', auth_views.LoginView, name='login'),
#    path('^logout/', auth_views.LogoutView, name='logout'),
#    path(r'^users/', include('djangotest.users.urls', namespace='users'),

    # Rest
#    path(r'^api/', include('djangotest.users.api.urls')),
#    path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider'))

    # Your stuff: custom urls includes go here
#] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
	"about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(r'^admin/', admin.site.urls),
    # User management

    path('^login/', auth_views.LoginView, name='login'),
    path('^logout/', auth_views.LogoutView, name='logout'),

    path(r'^users/', include(("djangotest.users.urls", "djanousers"), namespace="users")),

    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
	path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
	path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
	path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
