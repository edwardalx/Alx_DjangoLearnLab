from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    followers = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all())
    class Meta:
        model = CustomUser
        fields = ['username','password', 'first_name', 'last_name','bio','profile_picture','followers' ]

    def create(self, validated_data):
        followers = validated_data.pop('followers')
        user = CustomUser.objects.create(**validated_data)
        user.followers = followers
        Token.objects.get_or_create(user=user)
        return user

