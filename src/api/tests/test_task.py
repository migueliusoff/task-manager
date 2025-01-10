import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from api.models import Task
from api.tests.factories.task import TaskFactory
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


@pytest.mark.parametrize("is_empty", (True, False))
def test_task_list_success(api_client, is_empty):
    if not is_empty:
        task = TaskFactory.create()
    response = api_client.get(reverse("task-list"))
    assert response.status_code == status.HTTP_200_OK
    if is_empty:
        assert len(response.data) == 0
    else:
        assert len(response.data) == 1
        assert response.data[0]["id"] == task.id


@pytest.mark.parametrize("method", ("patch", "put"))
def test_task_update_success(api_client, method):
    task = TaskFactory.create()
    if method == "patch":
        data = {"title": "changed_string"}
        response = api_client.patch(reverse("task-detail", kwargs={"pk": task.id}), data=data)
    else:
        data = {
            "title": "changed_string",
            "description": task.description,
            "due_date": task.due_date,
            "user": task.user.id,
        }
        response = api_client.put(reverse("task-detail", kwargs={"pk": task.id}), data=data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == data["title"]


@pytest.mark.parametrize("method", ("patch", "put"))
@pytest.mark.parametrize("error", ("id", "data"))
def test_task_update_error(api_client, error, method):
    task = TaskFactory.create()
    data = {"user": 0}
    if method == "patch":
        if error == "id":
            response = api_client.patch(reverse("task-detail", kwargs={"pk": 0}))
        else:
            response = api_client.patch(reverse("task-detail", kwargs={"pk": task.id}), data=data)
    else:
        if error == "id":
            response = api_client.put(reverse("task-detail", kwargs={"pk": 0}))
        else:
            response = api_client.put(reverse("task-detail", kwargs={"pk": task.id}), data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST if error == "datat" else status.HTTP_404_NOT_FOUND


def test_task_delete_success(api_client):
    task = TaskFactory.create()
    response = api_client.delete(reverse("task-detail", kwargs={"pk": task.id}))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Task.objects.filter(id=task.id).exists()


def test_task_delete_error(api_client):
    TaskFactory.create()
    response = api_client.delete(reverse("task-detail", kwargs={"pk": 0}))
    assert response.status_code == status.HTTP_404_NOT_FOUND
