from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    followers = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all() )
    password = serializers.CharField()  # Hide password in responses
    class Meta:
        model = CustomUser
        fields = ['username','password', 'first_name', 'last_name','bio','profile_picture','followers' ]

    def create(self, validated_data):
        followers = validated_data.pop('followers')
        user = get_user_model().objects.create_user(**validated_data)
        user.followers = followers
        Token.objects.create(user=user)
        return user

