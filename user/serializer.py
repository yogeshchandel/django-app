from rest_framework import serializers
from django.contrib.auth.models import User
from .validator import validate_username, validate

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, validators=[validate_username, validate])
    password = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255, validators=[validate_username, validate])
    last_name = serializers.CharField(max_length=255, validators=[validate_username, validate])
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']