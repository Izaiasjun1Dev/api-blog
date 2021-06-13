from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from apps.authors.views import (
    AuthorViewSet
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('authors', AuthorViewSet, basename='Authors')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
