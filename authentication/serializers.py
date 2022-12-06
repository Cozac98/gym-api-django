from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model  # If used custom user model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True, min_length=7, max_length=8)
    password = serializers.CharField(write_only=True, min_length=8)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    is_staff = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        user = UserModel(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        

    class Meta:
        model = UserModel
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "is_staff"
        )

class StaffSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True, min_length=7, max_length=8)
    password = serializers.CharField(write_only=True, min_length=8)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    is_staff = serializers.BooleanField(default=True)

    def create(self, validated_data):
        user = UserModel(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff=validated_data['is_staff']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "is_staff"
        )