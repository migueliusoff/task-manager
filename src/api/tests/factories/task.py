import factory
from factory.django import DjangoModelFactory

from api.models import Task
from api.tests.factories.user import UserFactory


class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task

    title = factory.Faker("word")
    description = factory.Faker("text")
    due_date = factory.Faker("date")
    user = factory.SubFactory(UserFactory)
