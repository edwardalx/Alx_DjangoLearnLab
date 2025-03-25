from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    followers = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all())
    class Meta:
        model = CustomUser
        fields = ['username','password', 'first_name', 'last_name','bio','profile_picture','followers' ]

