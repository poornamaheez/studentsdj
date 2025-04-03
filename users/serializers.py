from rest_framework import serializers
from .models import UserCreds
from django.contrib.auth.hashers import make_password

class UserCredsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCreds
        fields = ['id', 'username', 'password']
    
    def validate_username(self, value):
        """Check if the username already exists before saving."""
        if UserCreds.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)