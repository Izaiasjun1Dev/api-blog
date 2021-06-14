from django.contrib.auth.hashers import (
    make_password, check_password
)
from rest_framework import serializers
from .models import Readers

class ReaderSerializers(serializers.ModelSerializer):
    """Serializes the data in the readers database"""
    class Meta:
        model = Readers
        fields = '__all__'

    def create(self, validated_data):
        """validates the password created by 
        the reader to authenticate itself creates a sha256 hash"""

        password = validated_data.pop('password')
        hash_pass = make_password(
                password=password, 
                salt=None, 
                hasher='pbkdf2_sha256'
            ) # Effectively convert password to hash
        
        reader = Readers.objects.create(
                password=hash_pass, **validated_data
            )

        return reader