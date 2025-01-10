from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Task, User
from api.serializers import TaskModelSerializer, UserModelSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    @swagger_auto_schema(method="get", responses={200: TaskModelSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def tasks(self, request, *args, **kwargs):
        return Response(TaskModelSerializer(self.get_object().tasks.all(), many=True).data)


class TaskViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
