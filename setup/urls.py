from apps.post.views import PostViewSet
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from apps.authors.views import (
    AuthorViewSet
)
from rest_framework_jwt.views import (
    obtain_jwt_token, refresh_jwt_token
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('authors', AuthorViewSet, basename='Authors')
router.register('posts', PostViewSet, basename='Posts')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', obtain_jwt_token),
    path('api/refresh-token/', refresh_jwt_token)
]
