from django.contrib.auth.hashers import (
    make_password, check_password
)
from rest_framework import serializers
from .models import Readers

class ReaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Readers
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        hash_pass = make_password(
                password=password, 
                salt=None, 
                hasher='pbkdf2_sha256'
            )
        
        reader = Readers.objects.create(
                password=hash_pass, **validated_data
            )

        return reader