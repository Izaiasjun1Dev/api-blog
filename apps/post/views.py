from rest_framework import (
    status,
    viewsets,
    generics
)
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from .models import Post

class PostViewSet(viewsets.ModelViewSet):
    """List and create Post"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'put', 'post', 'path']
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Capture the user id that created the post!"""
        
        serializer.save(author=self.request.user)