from rest_framework import serializers
from .models import CustomUserProfile

class CustomUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserProfile
        fields = ['avatar', 'alias']
