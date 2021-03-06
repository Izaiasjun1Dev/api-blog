from rest_framework import serializers
from .models import (
    Authors
)
class AuthorSerializer(serializers.ModelSerializer):
    """Serializador geral de dados de um author"""
    posts = serializers.PrimaryKeyRelatedField(
            many=True, read_only=True
        )
    class Meta:
        model = Authors
        fields = '__all__'

class AuthorPostSerializer(serializers.ModelSerializer):
    """Authors filter serializer"""
    class Meta:
        model = Authors
        fields = [
            'user_name',
            'first_name',
            'email',
            'avatar'
        ]        
 