from .models import Authors
from .serializers import AuthorSerializer
from rest_framework import (
    viewsets
)
from rest_framework.permissions import IsAuthenticated


class AuthorViewSet(viewsets.ModelViewSet):
    """List and create Authors"""
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer
    http_method_names = ['get', 'put', 'post', 'path']
    permission_classes = [IsAuthenticated]