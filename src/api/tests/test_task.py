import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from api.tests.factories.user import UserFactory


def test_task_create_success(api_client):
    user = UserFactory.create()
    data = {"title": "string", "description": "string", "due_date": "2025-01-10", "user": user.id}
    response = api_client.post(reverse("task-list"), data=data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["title"] == data["title"]


@pytest.mark.parametrize(
    "data",
    (
        {"title": "string", "description": "string", "due_date": "2025-01-10"},
        {"title": "string", "description": "string", "due_date": "2025-01-10", "user": 0},
    ),
)
def test_task_create_error(api_client, data):
    response = api_client.post(reverse("task-list"), data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
