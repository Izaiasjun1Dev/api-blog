from apps.authors.serializers import AuthorPostSerializer
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    author = AuthorPostSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'title_post',
            'post',
            'description',
            'author',
            'created_at',
            'updated_at'
        ]