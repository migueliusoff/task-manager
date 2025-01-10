from rest_framework import mixins, viewsets

from api.models import Task, User
from api.serializers import TaskModelSerializer, UserModelSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class TaskViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
