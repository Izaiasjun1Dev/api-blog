from apps.authors.serializers import AuthorPostSerializer
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """Serializes publications data to the database"""
    
    author = AuthorPostSerializer(read_only=True) # Binds the authores serializer for each post
    
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