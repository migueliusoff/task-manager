from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers

from api import views

schema_view = get_schema_view(
    openapi.Info(
        title="Task manager API",
        default_version="v1",
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register("users", views.UserViewSet, basename="user")
router.register("tasks", views.TaskViewSet, basename="task")

urlpatterns = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + router.urls
