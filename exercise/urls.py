from django.urls import path

from .views import ExerciseViewSet


urlpatterns = [
    path("", ExerciseViewSet.as_view({"get": "list", "post": "create"}), name="list-create-exercises"),
    path(
        "<int:pk>/",
        ExerciseViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="list-create-exercises",
    ),
]
