from rest_framework import mixins, viewsets

from api.models import User
from api.serializers import UserRegistrationModelSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationModelSerializer
