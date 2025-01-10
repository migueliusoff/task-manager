import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from api.tests.factories.user import UserFactory


def test_user_create_success(api_client):
    data = {"email": "test@test.ru", "username": "testtest"}
    response = api_client.post(reverse("user-list"), data=data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["username"] == data["username"]


@pytest.mark.parametrize("data", ({"email": "test@test.ru"}, {"email": "test@test.ru", "username": "testtest"}))
def test_user_create_error(api_client, data):
    if username := data.get("username"):
        UserFactory.create(username=username)

    response = api_client.post(reverse("user-list"), data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_user_get_success(api_client):
    user = UserFactory.create()
    response = api_client.get(reverse("user-detail", kwargs={"pk": user.pk}))
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == user.username


def test_user_get_error(api_client):
    response = api_client.get(reverse("user-detail", kwargs={"pk": 0}))
    assert response.status_code == status.HTTP_404_NOT_FOUND
