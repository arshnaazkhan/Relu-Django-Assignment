from rest_framework import serializers

from django.contrib.auth import get_user_model


User = get_user_model()

''' Serializer for getting student data'''

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'email']


''' Serializer to add a user '''

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

 
''' Reset Password serializer '''

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
