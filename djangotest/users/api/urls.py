from __future__ import absolute_import

from django.conf.urls import include, url, patterns
from rest_framework import routers

from ..views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = patterns('', url(r'^', include(router.urls)),)
