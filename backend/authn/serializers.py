from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model, login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
from .utils import get_tokens_for_user

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'last_login', 'is_active', 'is_staff')


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        login(self.context['request'], user)
        return user

    def to_representation(self, instance):
        representation = {}
        representation['tokens'] = get_tokens_for_user(instance)
        return representation


class UserLoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username_or_email = data['username_or_email']
        password = data['password']

        user = authenticate(username=username_or_email, password=password)
        if user is None:
            user = User.objects.get(email=username_or_email)
            if user is None:
                raise serializers.ValidationError("Invalid login credentials")
            user = authenticate(username=user.username, password=password)

        if not user.is_active:
            raise serializers.ValidationError('User account is disabled')

        login(self.context['request'], user)

        return {'tokens': get_tokens_for_user(user)}
