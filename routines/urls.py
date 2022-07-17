from django.urls import path

from .views import RoutineViewSet


urlpatterns = [
    path("", RoutineViewSet.as_view({"get": "list", "post": "create"}), name="list-create-routines"),
    path(
        "<int:pk>/",
        RoutineViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="retrieve-update-delete-routine",
    ),
]
