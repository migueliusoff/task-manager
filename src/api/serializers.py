from rest_framework import serializers

from api.models import User


class UserRegistrationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")
        read_only_fields = ("id",)
