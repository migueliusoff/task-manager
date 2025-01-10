from rest_framework import mixins, viewsets

from api.models import User
from api.serializers import UserRegistrationModelSerializer


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegistrationModelSerializer
