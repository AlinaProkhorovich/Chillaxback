from rest_framework import serializers
from django.contrib.auth import authenticate, models
from django.contrib.auth.models import User
from core.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            "id",
            "email",
            "username",
            "is_active",
            "is_superuser",
        ]


class RegistrationSerializer(UserSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    password_submit = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + [
            "password",
            "password_submit",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password_submit"]:
            raise serializers.ValidationError("Passwords unmatched")
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password_submit")
        return Profile.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }
