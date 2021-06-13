from apps.readers.models import Readers
from .serializers import ReaderSerializers
from rest_framework import (
    viewsets
)
from rest_framework.permissions import IsAuthenticated


class ReaderViewSet(viewsets.ModelViewSet):
    """List and create Readers"""
    queryset = Readers.objects.all()
    serializer_class = ReaderSerializers
    http_method_names =['get', 'put', 'post', 'path']
    permission_classes = [IsAuthenticated]