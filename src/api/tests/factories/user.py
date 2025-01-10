import factory

from api.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    username = factory.Faker("name")
