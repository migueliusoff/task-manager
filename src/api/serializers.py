from rest_framework import serializers

from api.models import Task, User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")
        read_only_fields = ("id",)


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "description", "due_date", "user")
        read_only_fields = ("id",)
